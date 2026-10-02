import base64,requests
from config import HF_API_KEY
API_URL="https://router.huggingface.co/v1/chat/completions"
HEADERS={"Authorization":f"Bearer{HF_API_KEY}","Content-Type":"application/json"}
MODELS=[
    "zai-org/GLM-4.5V",
    "Qwen/Qwen2.5-VL-72B-Insstruct",
    "Qwen/Qwen2.5-VL-32B-Insstruct",
    "google/gemma-3-27b-it",
]
def data_url(b:bytes)->str:
    return"data:image/jpeg;base64,"+base64.b64encode(b).decode("utf-8")
def extract_err(r:requests.Response)->str:
    try:
        j=r.json()
        return j.get("error",{}).get("message")or str(j)
    except Exception:
        return(r.text or "").strip()or r.reason or "Request failed."
def box(title:str,lines:list[str],icon:str):
    w=max(30,len(title+4,*(len(x) for x in lines)))
    w = max(30, len(title) + 4, *(len(x) for x in lines))
    print("\n" + "┏" + "━" * (w + 2) + "┓")
    print(f"┃ {icon} {title.ljust(w - 2)} ┃")
    print("┣" + "━" * (w + 2) + "┫")
    for x in lines:
        print(f"┃ {x.ljust(w)} ┃")
    print("┗" + "━" * (w + 2) + "┛\n")
def caption_single_image():    
    image_source=input("🖼️Enter image filename(default:test.jpg).strip()or"test.jpg"
                       