from ollama import AsyncClient

def get_client():
    return AsyncClient(host='http://localhost:11434')

#ollama run llama3.2
LLM_MODEL = 'llama3.2:1b'

system_prompt = (
        "You are translator. You must translate the user content to English. You must answer in English"
    )

async def stream(content: str):
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': content}
    ]
    
    async for part in await get_client().chat(model=LLM_MODEL, messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)


async def chat(content):
    message = {'role': 'user', 'content': content}
    response = await get_client().chat(model=LLM_MODEL, messages=[message])
    print(response.message.content)