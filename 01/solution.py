import utils

with open('input') as f:
    captcha = f.read().strip()

print(utils.reverse_captcha(captcha, 1))

print(utils.reverse_captcha(captcha, len(captcha) // 2))
