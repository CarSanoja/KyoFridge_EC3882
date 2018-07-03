/* ###################################################################
**     Filename    : main.c
**     Project     : led
**     Processor   : MC9S08QE128CLK
**     Version     : Driver 01.12
**     Compiler    : CodeWarrior HCS08 C Compiler
**     Date/Time   : 2018-05-05, 18:11, # CodeGen: 0
**     Abstract    :
**         Main module.
**         This module contains user's application code.
**     Settings    :
**     Contents    :
**         No public methods
**
** ###################################################################*/
/*!
** @file main.c
** @version 01.12
** @brief
**         Main module.
**         This module contains user's application code.
*/         
/*!
**  @addtogroup main_module main module documentation
**  @{
*/         
/* MODULE main */


/* Including needed modules to compile this module/procedure */
#include "Cpu.h"
#include "Events.h"
#include "AS1.h"
#include "AD1.h"
#include "TI1.h"
#include "Digital1.h"
#include "Digital2.h"
#include "Muestreo.h"
/* Include shared modules, which are used for whole project */
#include "PE_Types.h"
#include "PE_Error.h"
#include "PE_Const.h"
#include "IO_Map.h"


/* User includes (#include below this line is not maintained by Processor Expert) */
unsigned char estado=WAIT;
unsigned int cnt = 0;
bool read5 = FALSE;
bool trigger = TRUE;


void main(void)
{
  /* Write your local variable definition here */
	unsigned char error;
	unsigned char dummy;
	unsigned int ADC1, ADC2;
	bool dig1, dig2;
	char bitd1, bitd2;
	
	unsigned int Enviados5=5;
	unsigned int Enviados3=3;
	unsigned char trama5[5] = {0xF5,0x00,0x00,0x00,0x00};
	unsigned char trama3[3] = {0xF3,0x00,0x00};

  /*** Processor Expert internal initialization. DON'T REMOVE THIS CODE!!! ***/
  PE_low_level_init();
  /*** End of Processor Expert internal initialization.                    ***/

  /* Write your code here */
  /* For example: for(;;) { } */
  	  for (;;){
  		  
  		  /*Primero, se verifica si habrá que enviar 3 o 5 bytes en la trama*/
  		  if (cnt == 12000) {
  			  read5 = TRUE;	   // Habilita el envio y lectura de los 2 bytes del ch2 
  			  trigger = FALSE; // Deja de contar el interrupt
  		  }
  		  
  		  
  		  if (estado == MEDIR){
  			    			  
  			  //Sensor analogico 1
  			   			 
			  error	= AD1_MeasureChan(TRUE, 0);
			  error = AD1_GetChanValue16(0, &ADC1);
			  
			  //Sensor analogico 2, solo si se enviarán 5 datos
			  if (read5 == TRUE){ 
				  error	= AD1_MeasureChan(TRUE, 1);
				  error	= AD1_GetChanValue16(TRUE, &ADC2);
			  }
			  
			  //Digital 1
			  dig1 = Digital1_GetVal();
			  if (dig1 == TRUE){
				  bitd1 = 0x01;
			  }
			  else{
				  bitd1 = 0x00;
			  }
			  
			  //Digital 2

			  dig2 = Digital2_GetVal();
			  
			  if (dig2 == TRUE){
				  bitd2 = 0x01;
			  }
			  else{
				  bitd2 = 0x00;
			  }
		
			  /*Fin Medición*/
  			  
			  /*Inicio Comunicación Serial */
			  
			  trama3[1] = ((ADC1 >> 11) & 0x1F) + (bitd1 << 5) + (bitd2 << 6);
			  trama3[2] = (ADC1 >> 4 ) & 0x7F;
			  
			  // Si se enviarán 5 datos, agregar las lecturas del ADC N°2
			  if (read5 == TRUE ){
				  trama5[1] = trama3[1];
				  trama5[2] = trama3[2];				                     
				  trama5[3] = ((ADC2 >> 11) & 0x1F);
				  trama5[4] = (ADC2 >> 4 ) & 0x7F;
			  }
			  
			  // Si no se enviaran 5 bytes, enviar solo 3.
			  if (read5 == FALSE){
				  error = AS1_SendBlock(trama3, 3, &Enviados3);
			  }
			  else{
				  error = AS1_SendBlock(trama5, 5, &Enviados5);
			  }
			  
			  //Si se envió el escenario con 5 bytes
			  if (read5 == TRUE){
				  trigger = TRUE;
				  read5 = FALSE;
				  cnt = 0;
			  }
			  
			  /*Fin de Comunicación Serial*/
			  
			  
			//  error = AS1_ClearTxBuf(); //vaciado del buffer

			  estado = WAIT;  // cambio de estado hasta la otra medición
			  
			  
			  
			  
  		  }else{
  			  dummy = 1 ;
  			  
  		  }
  

}
  /*** Don't write any code pass this line, or it will be deleted during code generation. ***/
  /*** RTOS startup code. Macro PEX_RTOS_START is defined by the RTOS component. DON'T MODIFY THIS CODE!!! ***/
  #ifdef PEX_RTOS_START
    PEX_RTOS_START();                  /* Startup of the selected RTOS. Macro is defined by the RTOS component. */
  #endif
  /*** End of RTOS startup code.  ***/
  /*** Processor Expert end of main routine. DON'T MODIFY THIS CODE!!! ***/
  for(;;){}
  /*** Processor Expert end of main routine. DON'T WRITE CODE BELOW!!! ***/
} /*** End of main routine. DO NOT MODIFY THIS TEXT!!! ***/

/* END main */
/*!
** @}
*/
/*
** ###################################################################
**
**     This file was created by Processor Expert 10.3 [05.09]
**     for the Freescale HCS08 series of microcontrollers.
**
** ###################################################################
*/
