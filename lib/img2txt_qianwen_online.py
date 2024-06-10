from dashscope import MultiModalConversation
from http import HTTPStatus

def ui2html(image,prompt):
 
    # image file://D:/images/abc.png
    messages = [{
        'role': 'system',
        'content': [{
            'text': '你是一个优秀的网页设计师，可以根据UI图片制作html网页.'
        }]
    }, {
        'role':
        'user',
        'content': [
            {
                'image': image
            },
            {
                'text': prompt
            },
        ]
    }]
    responses = MultiModalConversation.call(model='qwen-vl-max', messages=messages,stream=True)
    return responses
    '''
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            yield response.output.choices[0].message.content[0].text
        else:
            yield response.message
    '''
