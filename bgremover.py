# from rembg import remove
# from PIL import Image
# import io

# input_path = "Dell 5400 04.jpeg"
# output_path = "output_white.jpg"

# # Step 1: Remove background
# with open(input_path, "rb") as i:
#     input_data = i.read()
#     output_data = remove(input_data)

# # Step 2: Convert to image
# img = Image.open(io.BytesIO(output_data)).convert("RGBA")

# # Step 3: Create white background
# white_bg = Image.new("RGB", img.size, (255, 255, 255))

# # Step 4: Paste image on white background
# white_bg.paste(img, mask=img.split()[3])  # use alpha channel

# # Step 5: Save final image
# white_bg.save(output_path, "JPEG")

# print("Background removed and set to white!")





# from google import genai
# import base64

# # Initialize client
# client = genai.Client(api_key="AIzaSyDNcFMK6PwY_6OUXj49ML5460SGQGosA70")

# # Read original image
# with open("Dell 5400 04.jpeg", "rb") as f:
#     original_image_bytes = f.read()

# # Encode to base64
# original_image_b64 = base64.b64encode(original_image_bytes).decode("utf-8")

# # Use generate_image() instead of generate_content()
# response = client.images.generate(
#     model="gemini-2.5-flash-image",
#     prompt="Replace the background of this image with solid white, keeping the subject intact.",
#     image=original_image_b64,
#     mask=None  # optional: you can provide a mask if you have one
# )

# # Get the generated image
# generated_image_b64 = response.data[0].b64_json
# generated_image_bytes = base64.b64decode(generated_image_b64)

# # Save output
# with open("output_white.png", "wb") as f:
#     f.write(generated_image_bytes)

# print("Image saved as output_white.png")











# pip install rembg[gpu,onnxruntime] pillow 
from rembg import remove, new_session
from PIL import Image

# Use 'birefnet-general' - it is much better at finding edges than the default
session = new_session("birefnet-general")

input_image = Image.open('my dp.jpg')

# Remove background
output_image = remove(input_image, session=session)

# Create white background
white_bg = Image.new("RGB", output_image.size, (255, 255, 255))
white_bg.paste(output_image, mask=output_image.split()[3])

white_bg.save("output_mydp.jpg", quality=100)
print("Saved with BiRefNet model.")