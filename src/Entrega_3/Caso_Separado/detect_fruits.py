import tensorflow as tf
import os


# load image
# similar to the method used for train/test, only here we read a jpeg image, not a tfrecords file
def read_image(image_path, image_reader):
    # A queue with the output strings. A QueueRunner for the Queue is added to the current Graph's QUEUE_RUNNER collection.
    filename_queue = tf.train.string_input_producer([image_path])
    _, image_file = image_reader.read(filename_queue)
    # Decode a JPEG-encoded image to a uint8 tensor.
    # The attr channels indicates the desired number of color channels for the decoded image.
    # Accepted values are:
    # 0: Use the number of channels in the JPEG-encoded image. DEFAULT
    # 1: output a grayscale image.
    # 3: output an RGB image.
    local_image = tf.image.decode_jpeg(image_file)
    # Convert image to dtype, scaling its values if needed.
    # Images that are represented using floating point values are expected to have values in the range [0,1). 
    local_image = tf.image.convert_image_dtype(local_image, tf.float32)
    # Se crean variables auxiliares para almacenar las imagenes a trabajar en escala de grises y color
    gray_image = tf.image.rgb_to_grayscale(local_image)
    local_image = tf.image.rgb_to_hsv(local_image)
    # This operation returns a 1-D integer tensor representing the shape of input
    shape = tf.shape(local_image)
    local_height = shape[0]
    local_width = shape[1]
    local_depth = shape[2]
    local_image = tf.reshape(local_image, [local_height, local_width, local_depth])
    # Se coloca en un solo tensor la informacion de color y escala de grises
    final_image = tf.concat([local_image, gray_image], 2)
    return final_image, local_height, local_width, local_depth + 1

def predict(sess, X, softmax, keep_prob, images):
    images = sess.run(images)
    # the result of running this method is an array of probabilities, where each index in the array corresponds to a label
    # he softmax function squashes the outputs of each unit to be between 0 and 1, just like a sigmoid function. 
    # But it also divides each output such that the total sum of the outputs is equal to 1 (check it on the figure above).
    # The output of the softmax function is equivalent to a categorical probability distribution, it tells you the 
    # probability that any of the classes are true.
    probability = sess.run(softmax, feed_dict={X: images, keep_prob: 1.0})
    # get the highest probability from the array and that should be the result
    print(probability)
    prediction = sess.run(tf.argmax(probability, 1))
    return prediction

def process_image(sess, X, softmax, keep_prob, image, image_height, image_width, image_depth,labels):
    image_depth = sess.run(image_depth)
    image_height = sess.run(image_height)
    image_width = sess.run(image_width)
    # resize the image to 100 x 100 pixels and shape it to be like an array of one image, since that is the required input 
    # for the network for smaller parts of an image and feed those to the network, tensorflow has a method called 
    # "extract_image_patches"
    img = tf.image.resize_images(tf.reshape(image, [1, image_height, image_width, image_depth]), [100, 100])
    img = tf.reshape(img, [-1, 100 * 100 * 4])
    rez = predict(sess, X, softmax, keep_prob, img)
    print('Label index: %d - Label: %s' % (rez, labels[rez[0]]))
    return labels[rez[0]]
    

def main():
    #import constants
    root_dir = os.getcwd() 
    # build an array of labels from the labels file so we can translate the result of the network to a human readable label
    with open(root_dir + '/labels') as f:
        labels = f.readlines()
    labels = [x.strip() for x in labels]
    labels =  labels

    # flag parsing
    tf.app.flags.DEFINE_string('image_path', root_dir + '/object.png', 'Path to image')
    FLAGS = tf.app.flags.FLAGS
    with tf.Session() as sess:
        image_path = FLAGS.image_path
        # To use, enqueue filenames in a Queue. The output of Read will be a filename (key) and the contents of that file (value).
        image_reader = tf.WholeFileReader()
        # restore the trained model from the saved checkpoint; provide the path to the meta file
        saver = tf.train.import_meta_graph(root_dir + '/fruit_models/model.ckpt.meta')
        # provide the path to the folder containing the checkpoints
        saver.restore(sess, tf.train.latest_checkpoint(root_dir + '/fruit_models'))
        graph = tf.get_default_graph()

        # to obtain a tensor from the saved model, we must get it by name, which is why we name the tensors when we create them
        # even if there is only one tensor with a name, in the meta and checkpoint files it is saved as an array, so we have to provide the index of the
        # tensor that we want to get -> thus we call "get_tensor_by_name(tensor_name:0)"

        # obtain the input tensor by name
        X = graph.get_tensor_by_name('X:0')
        # obtain the keep_prob tensor
        keep_prob = graph.get_tensor_by_name('keep_prob:0')
        # obtain the output layer by name and apply softmax on in in order to obtain an output of probabilities
        softmax = tf.nn.softmax(graph.get_tensor_by_name('softmax:0'))

        image, height, width, depth = read_image(image_path, image_reader)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        label_out = process_image(sess, X, softmax, keep_prob, image, height, width, depth, labels)

        coord.request_stop()
        coord.join(threads)
        sess.close()
    return label_out

#main()
