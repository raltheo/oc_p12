from app.controllers.mainmenu import start_app
import sentry_sdk
from app.middleware.auth import *
import signal
from app.utils import red_print, green_print

def signal_handler(sig, frame):
    red_print("\nAu revoir 😭!")
    green_print("A bientot 😉👋")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

sentry_sdk.init(
    dsn="https://10f6b9ece3ff41baa84800832963dda7@o4507180571885568.ingest.de.sentry.io/4507180575948880",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


start_app()
