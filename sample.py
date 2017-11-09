import requests
response = requests.get(
    "https://www.eventbriteapi.com/v3/users/me/owned_events/",
    headers={
        "Authorization": "Bearer SFOFD6ZZOA7TW6C26KZK",
    },
    verify=True,  # Verify SSL certificate
)
print response.json()
# ['events'][0]['name']['text']


#sample response
# {u'pagination': {u'object_count': 1, u'page_count': 1, u'page_number': 1, u'page_size': 50, u'has_more_items': False}, u'events': [{u'changed': u'2017-11-09T18:40:02Z', u'show_remaining': False, u'subcategory_id': None, u'is_series_parent': False, u'currency': u'USD', u'logo': {u'edge_color_set': True, u'edge_color': None, u'url': u'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F37570833%2F174511083986%2F1%2Foriginal.jpg?h=200&w=450&rect=0%2C0%2C362%2C181&s=d40d80a628816b13b6b027c3f5fa326b', u'id': u'37570833', u'crop_mask': {u'width': 362, u'height': 181, u'top_left': {u'y': 0, u'x': 0}}, u'aspect_ratio': u'2', u'original': {u'url': u'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F37570833%2F174511083986%2F1%2Foriginal.jpg?s=fd8cf675b40a64c63fd3e40e07163cdf', u'width': 628, u'height': 181}}, u'locale': u'en_US', u'id': u'39735538064', u'privacy_setting': u'unlocked', u'venue_id': u'22026632', u'end': {u'timezone': u'America/Los_Angeles', u'local': u'2017-12-19T22:00:00', u'utc': u'2017-12-20T06:00:00Z'}, u'source': u'create_2.0', u'capacity_is_custom': False, u'logo_id': u'37570833', u'start': {u'timezone': u'America/Los_Angeles', u'local': u'2017-12-19T19:00:00', u'utc': u'2017-12-20T03:00:00Z'}, u'version': u'3.0.0', u'listed': False, u'hide_end_date': False, u'status': u'live', u'description': {u'text': u'Fun fun fun!', u'html': u'<P>Fun fun fun!</P>'}, u'is_free': True, u'tx_time_limit': 480, u'capacity': 2, u'format_id': None, u'organizer_id': u'15708697507', u'name': {u'text': u'Test event', u'html': u'Test event'}, u'created': u'2017-11-09T18:39:59Z', u'is_locked': False, u'hide_start_date': False, u'url': u'https://www.eventbrite.com/e/test-event-tickets-39735538064', u'shareable': True, u'invite_only': False, u'online_event': False, u'is_series': False, u'category_id': None, u'is_reserved_seating': False, u'resource_uri': u'https://www.eventbriteapi.com/v3/events/39735538064/'}]}
