################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.local

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS_QUOTED += \
"../Generated_Code/AD1.c" \
"../Generated_Code/AS1.c" \
"../Generated_Code/Bit1.c" \
"../Generated_Code/Cpu.c" \
"../Generated_Code/Digital2.c" \
"../Generated_Code/IO_Map.c" \
"../Generated_Code/KB1.c" \
"../Generated_Code/LedTrama5.c" \
"../Generated_Code/Led_Dig_1.c" \
"../Generated_Code/Led_Dig_2.c" \
"../Generated_Code/Muestreo.c" \
"../Generated_Code/TI1.c" \
"../Generated_Code/Vectors.c" \

C_SRCS += \
../Generated_Code/AD1.c \
../Generated_Code/AS1.c \
../Generated_Code/Bit1.c \
../Generated_Code/Cpu.c \
../Generated_Code/Digital2.c \
../Generated_Code/IO_Map.c \
../Generated_Code/KB1.c \
../Generated_Code/LedTrama5.c \
../Generated_Code/Led_Dig_1.c \
../Generated_Code/Led_Dig_2.c \
../Generated_Code/Muestreo.c \
../Generated_Code/TI1.c \
../Generated_Code/Vectors.c \

OBJS += \
./Generated_Code/AD1_c.obj \
./Generated_Code/AS1_c.obj \
./Generated_Code/Bit1_c.obj \
./Generated_Code/Cpu_c.obj \
./Generated_Code/Digital2_c.obj \
./Generated_Code/IO_Map_c.obj \
./Generated_Code/KB1_c.obj \
./Generated_Code/LedTrama5_c.obj \
./Generated_Code/Led_Dig_1_c.obj \
./Generated_Code/Led_Dig_2_c.obj \
./Generated_Code/Muestreo_c.obj \
./Generated_Code/TI1_c.obj \
./Generated_Code/Vectors_c.obj \

OBJS_QUOTED += \
"./Generated_Code/AD1_c.obj" \
"./Generated_Code/AS1_c.obj" \
"./Generated_Code/Bit1_c.obj" \
"./Generated_Code/Cpu_c.obj" \
"./Generated_Code/Digital2_c.obj" \
"./Generated_Code/IO_Map_c.obj" \
"./Generated_Code/KB1_c.obj" \
"./Generated_Code/LedTrama5_c.obj" \
"./Generated_Code/Led_Dig_1_c.obj" \
"./Generated_Code/Led_Dig_2_c.obj" \
"./Generated_Code/Muestreo_c.obj" \
"./Generated_Code/TI1_c.obj" \
"./Generated_Code/Vectors_c.obj" \

C_DEPS += \
./Generated_Code/AD1_c.d \
./Generated_Code/AS1_c.d \
./Generated_Code/Bit1_c.d \
./Generated_Code/Cpu_c.d \
./Generated_Code/Digital2_c.d \
./Generated_Code/IO_Map_c.d \
./Generated_Code/KB1_c.d \
./Generated_Code/LedTrama5_c.d \
./Generated_Code/Led_Dig_1_c.d \
./Generated_Code/Led_Dig_2_c.d \
./Generated_Code/Muestreo_c.d \
./Generated_Code/TI1_c.d \
./Generated_Code/Vectors_c.d \

C_DEPS_QUOTED += \
"./Generated_Code/AD1_c.d" \
"./Generated_Code/AS1_c.d" \
"./Generated_Code/Bit1_c.d" \
"./Generated_Code/Cpu_c.d" \
"./Generated_Code/Digital2_c.d" \
"./Generated_Code/IO_Map_c.d" \
"./Generated_Code/KB1_c.d" \
"./Generated_Code/LedTrama5_c.d" \
"./Generated_Code/Led_Dig_1_c.d" \
"./Generated_Code/Led_Dig_2_c.d" \
"./Generated_Code/Muestreo_c.d" \
"./Generated_Code/TI1_c.d" \
"./Generated_Code/Vectors_c.d" \

OBJS_OS_FORMAT += \
./Generated_Code/AD1_c.obj \
./Generated_Code/AS1_c.obj \
./Generated_Code/Bit1_c.obj \
./Generated_Code/Cpu_c.obj \
./Generated_Code/Digital2_c.obj \
./Generated_Code/IO_Map_c.obj \
./Generated_Code/KB1_c.obj \
./Generated_Code/LedTrama5_c.obj \
./Generated_Code/Led_Dig_1_c.obj \
./Generated_Code/Led_Dig_2_c.obj \
./Generated_Code/Muestreo_c.obj \
./Generated_Code/TI1_c.obj \
./Generated_Code/Vectors_c.obj \


# Each subdirectory must supply rules for building sources it contributes
Generated_Code/AD1_c.obj: ../Generated_Code/AD1.c
	@echo 'Building file: $<'
	@echo 'Executing target #4 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/AD1.args" -ObjN="Generated_Code/AD1_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/%.d: ../Generated_Code/%.c
	@echo 'Regenerating dependency file: $@'
	
	@echo ' '

Generated_Code/AS1_c.obj: ../Generated_Code/AS1.c
	@echo 'Building file: $<'
	@echo 'Executing target #5 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/AS1.args" -ObjN="Generated_Code/AS1_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Bit1_c.obj: ../Generated_Code/Bit1.c
	@echo 'Building file: $<'
	@echo 'Executing target #6 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Bit1.args" -ObjN="Generated_Code/Bit1_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Cpu_c.obj: ../Generated_Code/Cpu.c
	@echo 'Building file: $<'
	@echo 'Executing target #7 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Cpu.args" -ObjN="Generated_Code/Cpu_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Digital2_c.obj: ../Generated_Code/Digital2.c
	@echo 'Building file: $<'
	@echo 'Executing target #8 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Digital2.args" -ObjN="Generated_Code/Digital2_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/IO_Map_c.obj: ../Generated_Code/IO_Map.c
	@echo 'Building file: $<'
	@echo 'Executing target #9 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/IO_Map.args" -ObjN="Generated_Code/IO_Map_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/KB1_c.obj: ../Generated_Code/KB1.c
	@echo 'Building file: $<'
	@echo 'Executing target #10 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/KB1.args" -ObjN="Generated_Code/KB1_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/LedTrama5_c.obj: ../Generated_Code/LedTrama5.c
	@echo 'Building file: $<'
	@echo 'Executing target #11 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/LedTrama5.args" -ObjN="Generated_Code/LedTrama5_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Led_Dig_1_c.obj: ../Generated_Code/Led_Dig_1.c
	@echo 'Building file: $<'
	@echo 'Executing target #12 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Led_Dig_1.args" -ObjN="Generated_Code/Led_Dig_1_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Led_Dig_2_c.obj: ../Generated_Code/Led_Dig_2.c
	@echo 'Building file: $<'
	@echo 'Executing target #13 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Led_Dig_2.args" -ObjN="Generated_Code/Led_Dig_2_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Muestreo_c.obj: ../Generated_Code/Muestreo.c
	@echo 'Building file: $<'
	@echo 'Executing target #14 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Muestreo.args" -ObjN="Generated_Code/Muestreo_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/TI1_c.obj: ../Generated_Code/TI1.c
	@echo 'Building file: $<'
	@echo 'Executing target #15 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/TI1.args" -ObjN="Generated_Code/TI1_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '

Generated_Code/Vectors_c.obj: ../Generated_Code/Vectors.c
	@echo 'Building file: $<'
	@echo 'Executing target #16 $<'
	@echo 'Invoking: HCS08 Compiler'
	"$(HC08ToolsEnv)/chc08" -ArgFile"Generated_Code/Vectors.args" -ObjN="Generated_Code/Vectors_c.obj" "$<" -Lm="$(@:%.obj=%.d)" -LmCfg=xilmou
	@echo 'Finished building: $<'
	@echo ' '


