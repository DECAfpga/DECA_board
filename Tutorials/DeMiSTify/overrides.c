
// Initial ROM 
const char *bootrom_name="NEXT186 ROM";


// Initial VHD
extern unsigned char romtype=0;
char *autoboot()
{
	char *result=0;
	romtype=0;
	if(!LoadROM(bootrom_name))
		result="ROM loading failed";
	loadimage("NEXT186 VHD",0);
	return(result);
}

//NOTE: if having problems loading VHD you could try to load first VHD and then the ROM


/*-------- ALTERNATIVE WAY ---------*/

#include "diskimg.h"

const char *bootvhd_name="NEXT186 VHD";
const char *bootrom_name="NEXT186 ROM";

char *autoboot()
{
        char *result=0;
	if(!LoadROM(bootrom_name))
		result="ROM loading failed";
        diskimg_mount(bootvhd_name,0);
        return(result);
}

