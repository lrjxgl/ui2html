import gradio as gr
from http import HTTPStatus
#import lib.img2txt_minicpm as img2txt
import lib.img2txt_qianwen_online as img2txt 
'''
prompt="""
    根据图片生成html代码，只需返回HTMl和css代码,不需要过多解释
""" 
''' 
def ui2html(imgList,prompt) :
   
    #return img2txt.ui2html(image,prompt)
    for img in imgList:
        print(img[0])
        image=img[0]
        responses=img2txt.ui2html(image,prompt)
        for response in responses:
            if response.status_code == HTTPStatus.OK:
                print(response.output.choices[0].message.content)
                yield response.output.choices[0].message.content[0]["text"]
            else:
                yield response.message
            
with gr.Blocks() as demo:
    gr.Markdown("""
    # UI2HTML
    根据图片生成html代码，目前对于小图片效果较好，所以先切图再上传
    """)
    with gr.Row():
        with gr.Column():
            imgList=gr.Gallery(label="上传UI 图片",height=400,type="filepath",value=[])
            prompt=gr.Textbox(label="prompt",value="根据图片生成完整地html代码，无需js.")
            btn=gr.Button("生成html代码")
        text=gr.Markdown(label="html代码")
        
    btn.click(fn=ui2html,inputs=[imgList,prompt],outputs=text)
   
demo.launch(server_name='0.0.0.0')