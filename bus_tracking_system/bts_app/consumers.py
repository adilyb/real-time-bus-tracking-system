from channels.generic.websocket import AsyncWebsocketConsumer
import json

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'bus_tracking'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        latitude = text_data_json['latitude']
        longitude = text_data_json['longitude']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'location_message',
                'latitude': latitude,
                'longitude': longitude,
            }
        )

    async def location_message(self, event):
        latitude = event['latitude']
        longitude = event['longitude']

        await self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude': longitude,
        }))
