#ifndef EVENT_PARSER_H
#define EVENT_PARSER_H
#include <stddef.h>
#include <stdint.h>
#define EVENT_START_BYTE 0x7Eu
#define EVENT_END_BYTE 0x7Fu
#define EVENT_MAX_PAYLOAD 32u
typedef enum { EVENT_WAIT_START, EVENT_IN_FRAME, EVENT_OVERFLOW } event_parser_state_t;
typedef enum { EVENT_NEED_MORE, EVENT_FRAME_READY, EVENT_REJECTED } event_result_t;
typedef struct { event_parser_state_t state; uint8_t payload[EVENT_MAX_PAYLOAD]; size_t length; } event_parser_t;
void event_parser_init(event_parser_t *parser);
event_result_t event_parser_feed(event_parser_t *parser, uint8_t byte, const uint8_t **payload, size_t *length);
#endif
