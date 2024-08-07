import json
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def handle_webapp_data(update, context):
    data = json.loads(update.effective_message.web_app_data.data)
    if data['action'] == 'search':
        query = data['query']
        # Make the API request
        api_url = f"https://data.unwrangle.com/api/getter/?platform=amazon_search&search={query}&country_code=es&page=1&api_key=YOUR_API_KEY"
        response = requests.get(api_url)
        results = response.json()

        # Format and send results
        message = "Search Results:\n\n"
        for item in results[:5]:  # Limit to 5 results
            message += f"{item['title']} - {item['price']}\n\n"

        update.effective_message.reply_text(message)

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.status_update.web_app_data, handle_webapp_data))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
