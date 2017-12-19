def reverse_captcha(captcha, step):
    result = 0
    for i in range(len(captcha)):
        compare_to = (i + step) % (len(captcha))
        if captcha[i] == captcha[compare_to]:
            result += int(captcha[i])
    return result
