import asyncio, os, base64
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage

load_dotenv("/app/backend/.env")
api_key = os.getenv("EMERGENT_LLM_KEY")
assert api_key, "missing key"

os.makedirs("/app/scripts/lifestyle", exist_ok=True)

STYLE = ("Photorealistic high-end editorial food photography, vertical portrait 3:4 composition, "
         "warm natural light, shallow depth of field, premium food magazine style, "
         "warm ivory and caramel tones, no text, no words, no logos, no watermarks.")

SCENES = {
  "beverage": "Close-up, clean image of rich, dark amber liquid palm sugar being carefully drizzled from a spoon into a tall glass of iced coffee with gentle cream swirls, minimalist cafe background softly blurred.",
  "dessert": "Beautifully plated coconut panna cotta dessert covered with a generous pooling of dark palm sugar sauce on a light-colored porcelain plate, elegant minimal styling.",
  "cooking": "Clean, minimalist shot of a chef's hand stirring a thick, glossy palm sugar caramel glaze in a pan over a gas burner, fresh herbs and spices softly blurred in the background.",
  "baking": "Freshly baked golden palm sugar cookies cooling on a wire rack over a warm wooden countertop, with a small bowl of palm sugar powder and measuring spoons nearby.",
  "service": "Professionally set up B2B catering service table featuring clean glass dispensers of different palm sugar varieties and neatly arranged serving bowls and spoons, ready for an event, elegant and organized.",
}

async def gen(name, scene):
    chat = LlmChat(api_key=api_key, session_id="psl-" + name,
                   system_message="You are a professional food photography image generator.")
    chat.with_model("gemini", "gemini-3.1-flash-image-preview").with_params(modalities=["image", "text"])
    msg = UserMessage(text=scene + " " + STYLE)
    text, images = await chat.send_message_multimodal_response(msg)
    if not images:
        print(name, "FAILED: no images", flush=True)
        return False
    raw = base64.b64decode(images[0]["data"])
    with open(f"/app/scripts/lifestyle/{name}.png", "wb") as f:
        f.write(raw)
    print(name, "OK", len(raw), "bytes", flush=True)
    return True

async def main():
    results = await asyncio.gather(*[gen(n, s) for n, s in SCENES.items()])
    print("ALL DONE", sum(results), "/5", flush=True)

asyncio.run(main())
