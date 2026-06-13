#include "event_parser.h"
#include <stdio.h>
int main(void){ event_parser_t p; event_parser_init(&p); const uint8_t *out; size_t len; uint8_t f[]={EVENT_START_BYTE,'O','K',EVENT_END_BYTE}; for(size_t i=0;i<sizeof f;i++){ if(event_parser_feed(&p,f[i],&out,&len)==EVENT_FRAME_READY) printf("%zu\n",len);} }
