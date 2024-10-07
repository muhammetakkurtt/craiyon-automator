import asyncio
import json
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from selenium_driverless.scripts.network_interceptor import NetworkInterceptor, InterceptedRequest, RequestPattern
from cdp_patches.input import AsyncInput
# Global flag to start capturing requests after button click
capture_requests = False

# Function to handle intercepted requests
async def on_request(data: InterceptedRequest):
    global capture_requests, current_prompt
    if capture_requests and "img.craiyon.com" in data.request.url and data.request.url.endswith(".webp"):
        print(f"Captured Image URL: {data.request.url}")
        if current_prompt in image_urls:
            image_urls[current_prompt].append(data.request.url)
    await data.continue_request()

async def main(prompts):
    global capture_requests, image_urls, current_prompt
    image_urls = {}
    current_prompt = ""

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1265,1420")
    # Initialize the WebDriver with NetworkInterceptor
    async with webdriver.Chrome(options=options, max_ws_size=2**30) as driver:
        async with NetworkInterceptor(driver, on_request=on_request, patterns=[RequestPattern.AnyRequest]) as interceptor:

            # Navigate to the Craiyon website
            await driver.get('https://www.craiyon.com/', wait_load=True)
            await driver.sleep(2)  # Wait for the page to load completely

            for prompt in prompts:
                current_prompt = prompt
                image_urls[prompt] = []

                # Locate the textarea and send a prompt
                textarea = await driver.find_element(By.ID, 'prompt')
                await textarea.clear()  # Clear previous prompt
                await textarea.send_keys(prompt)

                # Locate the "Draw" button by its ID and click it
                generate_button = await driver.find_element(By.ID, 'generateButton')
                # Set the flag to capture requests after the button is clicked
                capture_requests = True
                await generate_button.click()
                await driver.sleep(5)

                # Specify the coordinates of the checkbox box
                x1, y1, x2, y2 = 495, 664, 515, 703
                x = (x1 + x2) // 2
                y = (y1 + y2) // 2

                async_input = await AsyncInput(browser=driver)

                try:
                    await async_input.click("left", x, y)
                    print(f"Click performed. Coordinates: ({x}, {y})")
                except Exception as e:
                    print(f"Error occurred during click: {str(e)}")

                # Wait for 70 seconds to allow time for image generation
                await driver.sleep(70)


                with open("generated_images.json", "w") as json_file:
                    json.dump(image_urls, json_file, indent=4)

                print(f"Results for '{prompt}' saved to generated_images.json file.")

    print("All prompts processed and results saved.")
