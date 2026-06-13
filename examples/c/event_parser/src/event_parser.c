#include "event_parser.h"
#include <string.h>

void event_parser_init(event_parser_t *parser) {
    if (parser) {
        parser->state = EVENT_WAIT_START;
        parser->length = 0;
        memset(parser->payload, 0, sizeof parser->payload);
    }
}

event_result_t event_parser_feed(event_parser_t *parser, uint8_t byte, const uint8_t **payload, size_t *length) {
    if (!parser || !payload || !length) {
        return EVENT_REJECTED;
    }
    *payload = NULL;
    *length = 0;
    if (byte == EVENT_START_BYTE) {
        parser->state = EVENT_IN_FRAME;
        parser->length = 0;
        return EVENT_NEED_MORE;
    }
    if (parser->state == EVENT_WAIT_START) {
        return EVENT_NEED_MORE;
    }
    if (parser->state == EVENT_OVERFLOW) {
        if (byte == EVENT_END_BYTE) {
            event_parser_init(parser);
        }
        return EVENT_REJECTED;
    }
    if (byte == EVENT_END_BYTE) {
        *payload = parser->payload;
        *length = parser->length;
        parser->state = EVENT_WAIT_START;
        return EVENT_FRAME_READY;
    }
    if (parser->length >= EVENT_MAX_PAYLOAD) {
        parser->state = EVENT_OVERFLOW;
        parser->length = 0;
        return EVENT_REJECTED;
    }
    parser->payload[parser->length++] = byte;
    return EVENT_NEED_MORE;
}
