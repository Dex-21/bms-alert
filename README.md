# bms-alert

A small script that checks a BookMyShow movie page every 5 minutes using GitHub Actions and sends a Telegram message when bookings appear. It only watches the page. Booking is done by hand.

## Files

- `alert.py`: checks the page once and sends a Telegram alert if "Book tickets" is found
- `.github/workflows/alert.yml`: runs `alert.py` every 5 minutes

## Setup

1. Create a Telegram bot with @BotFather and copy the token.
2. Get your chat ID from @userinfobot, then press **Start** on your new bot.
3. Copy the BookMyShow movie page URL for your city.
4. In the repo go to **Settings → Secrets and variables → Actions** and add:

| Secret | Value |
|--------|-------|
| `BMS_URL` | BookMyShow movie page link |
| `BOT_TOKEN` | Telegram bot token |
| `CHAT_ID` | Your Telegram numeric ID |

5. Open the **Actions** tab, select **bms-alert**, and click **Run workflow** to test.

## Notes

- Scheduled runs can be delayed by a few minutes.
- If the logs show `403`, BookMyShow is blocking GitHub's servers. Run the script on your own phone or PC instead.
- After you get the alert, disable the workflow (Actions → bms-alert → ⋯ → Disable workflow) so it stops pinging you.
- Never commit your bot token or URL into the code. Keep them in secrets.

## Disclaimer

For personal use only. This does not book tickets or bypass any limits.
