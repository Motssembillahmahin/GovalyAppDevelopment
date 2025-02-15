from kivy.uix.button import Button

class Button4(Button):
    def __init__(self, db, update_callback, **kwargs):
        super().__init__(text="Reset Total", **kwargs)
        self.db = db
        self.update_callback = update_callback
        self.bind(on_press=self.reset_total)

    def reset_total(self, instance):
        """ ✅ Resets the total sum to 0 and updates the UI immediately. """
        if self.db:
            self.db.reset_sum()  # ✅ Ensure database total is reset
            self.update_callback()  # ✅ Update UI to reflect the reset sum
        else:
            print("❌ ERROR: Database connection is missing in Button4!")
