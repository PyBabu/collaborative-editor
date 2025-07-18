# editor/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Document
from asgiref.sync import sync_to_async

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope['url_route']['kwargs']['doc_id']
        self.room_group_name = f'doc_{self.doc_id}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Save content to DB
        await self.save_document_content(self.doc_id, message)

        # Send to all connected users
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'document_edit',
                'message': message
            }
        )

    async def document_edit(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))

    @sync_to_async
    def save_document_content(self, doc_id, content):
        doc = Document.objects.get(id=doc_id)
        doc.content = content
        doc.save()
