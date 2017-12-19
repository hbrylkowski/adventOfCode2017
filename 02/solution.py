import utils

with open('input') as f:
    captcha = f.read().strip()

print(utils.checksum(captcha, "\t"))
print(utils.checksum_modulo(captcha, "\t"))

