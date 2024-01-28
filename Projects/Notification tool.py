from plyer import notification
import time

def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    # Example usage
    notification_title = "Reminder"
    notification_message = "It's time to take a break!"

    desktop_notifier(notification_title, notification_message)

    # Optionally, you can schedule multiple notifications
    for _ in range(3):
        time.sleep(1800)  # Sleep for 30 minutes
        desktop_notifier(notification_title, notification_message)
