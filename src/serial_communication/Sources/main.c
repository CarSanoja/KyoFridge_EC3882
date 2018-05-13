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
/* Include shared modules, which are used for whole project */
#include "PE_Types.h"
#include "PE_Error.h"
#include "PE_Const.h"
#include "IO_Map.h"

/* User includes (#include below this line is not maintained by Processor Expert) */

void main(void)
{
  /* Write your local variable definition here */
	unsigned char error;
	typedef union{
		unsigned char u8[2];
		unsigned int u16;
	}VALOR;
	volatile VALOR iADC, aux1, iADC2, aux2;
	unsigned int Enviados=2;
	unsigned char tADC[5] = {0xF5,0x60,0x00,0x00,0x00};
	int i=0;
	volatile int d1;
	
	/* Define LED's ON or OFF,*/
	#define ON 1
	#define OFF 0
	/* Define LED's*/
	#define LED1 PTCD_PTCD0
	/*Define Switch 1*/
	#define SW1 PTAD_PTAD2
	PTADD = 0xFB;  /*PortA bit 2 input all others outputs */
	PTCDD = 0xFF;  /*all port C outputs */
	PTCD = 0xFF;   /* turn off all LEDs */
	PTAPE = 0x04;  /*enable pullup on PTA bit 2 */
  /*** Processor Expert internal initialization. DON'T REMOVE THIS CODE!!! ***/
  PE_low_level_init();
  /*** End of Processor Expert internal initialization.                    ***/

  /* Write your code here */
  /* For example: for(;;) { } */
for (;;){

  //Sensor analogico 1
	  do{
		  error	= AD1_MeasureChan(TRUE, 0);
		  }while(error!=ERR_OK);
	  do{
		  error = AD1_GetChanValue16(0, &iADC);
	  }while(error!=ERR_OK);
	  iADC.u16 = iADC.u16 >> 4;
	  iADC.u16 = iADC.u16 & 0xFFF;
	  // Ahora se debe colocar los 12 bits en formato de la trama
	  // los ultimos 4 bits los obtenemos haciendo shift de 7 a la derecha
	  aux1.u16 = iADC.u16 >> 7;
	  aux1.u16 = aux1.u16 & 0x1F; // Aqui estan los primeros 5 bits
	  iADC.u16 = iADC.u16 & 0x7F; // Aqui estan los otros 7 bits
	  tADC[1] = tADC[1] | aux1.u16; // Se guardan los 5 bits
	  tADC[2] = tADC[2] | iADC.u16; //Se guardan los 7 bits
	  
	  
	  //Sensor analogico 2
	  do{
	  	error	= AD1_MeasureChan(TRUE, 1);
	  	}while(error!=ERR_OK);
	  do{
	  	error = AD1_GetChanValue16(1, &iADC2);
	  }while(error!=ERR_OK);
	  iADC2.u16 = iADC2.u16 >> 4;
	  iADC2.u16 = iADC2.u16 & 0xFFF;
	  // Ahora se debe colocar los 12 bits en formato de la trama
	  // los ultimos 4 bits los obtenemos haciendo shift de 7 a la derecha
	  aux2.u16 = iADC2.u16 >> 7;
	  aux2.u16 = aux2.u16 & 0x1F; // Aqui estan los primeros 5 bits
	  iADC2.u16 = iADC2.u16 & 0x7F; // Aqui estan los otros 7 bits
	  tADC[3] = tADC[3] | aux2.u16; // Se guardan los 5 bits
	  tADC[4] = tADC[4] | iADC2.u16; //Se guardan los 7 bits
	    
  
	  //Sensor digital 1
	  if (SW1) {
		  LED1 = ON;
		  d1 = 0x5F;
	  } else {LED1 = OFF;d1 = 0x1F;}
	  tADC[1] = tADC[1] & d1;
	  
	
	  
	  if (i==0){
	  error = AS1_SendChar(tADC[0]);
	  i=i+1;
	  }
	  else if (i==1){
	  error = AS1_SendChar(tADC[1]);
	  tADC[1] = 0x1F;
	  i=i+1;}
	  else if (i==2){
	  error = AS1_SendChar(tADC[2]);
	  i=i+1;}
	  else if (i==3){
	  error = AS1_SendChar(tADC[3]);
	  i=i+1;}
	  else{
	  error = AS1_SendChar(tADC[4]);
	  i=0;}
	  
  

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
