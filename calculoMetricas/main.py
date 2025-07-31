vp = 100 
vn = 900
fp = 50
fn = 75

def sensibilidade(vp, fn):
    try:
        return vp / (vp + fn) 
    except ZeroDivisionError:
        return 0.0
    
def especificidade(vn, fp):
    try:    
        return vn / (fp + vn)
    except ZeroDivisionError:
        return 0.0

def acuracia(vp, vn, fp, fn):
    try:
        total = vp + vn + fp + fn
        return (vp + vn) / total
    except ZeroDivisionError:
        return 0.0

def precisao(vp, fp):
    try:
        return vp / (vp + fp)
    except ZeroDivisionError:
        return 0.0
    
def fScore(precisao, sensibilidade):
    try:
        return (2 * (precisao(vp, fp) * sensibilidade(vp, fn))) / (precisao(vp, fp) + sensibilidade(vp, fn))
    except ZeroDivisionError:
        return 0.0

print(f'Sensibilidade: {sensibilidade(vp, fn):.5f}')
print(f'Especificidade: {especificidade(vn, fp):.5f}')
print(f'Acurácia: {acuracia(vp, vn, fp, fn):.5f}')
print(f'Precisão: {precisao(vp, fp):.5f}')
print(f'F-Score: {fScore(precisao, sensibilidade):.5f}')

