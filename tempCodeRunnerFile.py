    mistakes += 1
    if mistakes > 6:
        btn.configure(state="disabled")
        default.GameOverAnimation()
        keyboard.disabled()
    else:
        default.WrongAnswer(mistakes)