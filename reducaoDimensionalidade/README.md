cv2.imread()

    Funcionalidade: Carrega uma imagem a partir de um arquivo especificado.

    Sintaxe: cv2.imread(filepath, flags)

    Parâmetros:

        filepath (string): O caminho para o arquivo de imagem (ex: 'imagem_colorida.jpg').

        flags (int, opcional): Especifica o modo como a imagem deve ser lida. Os mais comuns são:

            cv2.IMREAD_COLOR (ou 1): Carrega a imagem colorida. Qualquer transparência é ignorada. É o padrão.

            cv2.IMREAD_GRAYSCALE (ou 0): Carrega a imagem em modo de tons de cinza.

    Retorno:

        Retorna um objeto NumPy array representando a imagem.

        Se a imagem não puder ser lida (arquivo não encontrado, permissões incorretas, formato inválido), a função retorna None.

cv2.cvtColor()

    Funcionalidade: Converte uma imagem de um espaço de cores para outro.

    Sintaxe: cv2.cvtColor(src, code)

    Parâmetros:

        src (NumPy array): A imagem de origem que será convertida.

        code (int): O código de conversão do espaço de cores. Para este script, usamos cv2.COLOR_BGR2GRAY para converter de BGR (padrão do OpenCV) para tons de cinza.

    Retorno:

        A imagem convertida, também como um NumPy array.

cv2.threshold()

    Funcionalidade: Aplica uma limiarização de valor fixo a uma imagem em tons de cinza. É o coração da conversão para preto e branco.

    Sintaxe: cv2.threshold(src, thresh, maxval, type)

    Parâmetros:

        src (NumPy array): A imagem de origem, que deve ser em tons de cinza.

        thresh (float): O valor do limiar. Pixels com intensidade abaixo deste valor serão tratados de uma forma, e os acima, de outra.

        maxval (float): O valor máximo a ser atribuído aos pixels que ultrapassam o limiar. Geralmente 255 (branco).

        type (int): O tipo de limiarização a ser aplicado. No script usamos:

            cv2.THRESH_BINARY: Se pixel_value > thresh, o novo valor é maxval. Caso contrário, é 0.

            cv2.THRESH_OTSU: Um flag adicional que pode ser combinado com outros tipos (ex: cv2.THRESH_BINARY + cv2.THRESH_OTSU). Quando usado, o algoritmo de Otsu determina o valor de thresh ideal automaticamente, e o valor thresh que você passou como parâmetro é ignorado.

    Retorno:

        Uma tupla com dois valores: (retval, dst).

            retval (float): O valor do limiar que foi efetivamente utilizado (seja o que você passou ou o calculado por Otsu).

            dst (NumPy array): A imagem binarizada resultante.

cv2.imwrite()

    Funcionalidade: Salva uma imagem em um arquivo.

    Sintaxe: cv2.imwrite(filename, img)

    Parâmetros:

        filename (string): O nome do arquivo a ser salvo, incluindo a extensão (ex: 'imagem_salva.png'). A extensão determina o formato de codificação.

        img (NumPy array): A imagem a ser salva.

    Retorno:

        Retorna True se a imagem for salva com sucesso e False em caso de falha.

cv2.imshow()

    Funcionalidade: Exibe uma imagem em uma janela na tela. A janela se ajusta automaticamente ao tamanho da imagem.

    Sintaxe: cv2.imshow(winname, mat)

    Parâmetros:

        winname (string): O nome (título) da janela.

        mat (NumPy array): A imagem a ser exibida.

    Retorno:

        Nenhum.

cv2.waitKey()

    Funcionalidade: Aguarda por um tempo determinado (em milissegundos) por um pressionamento de tecla.

    Sintaxe: cv2.waitKey(delay)

    Parâmetros:

        delay (int): O tempo de espera em milissegundos. Se o valor for 0, a função espera indefinidamente até que qualquer tecla seja pressionada.

    Retorno:

        O código da tecla pressionada ou -1 se nenhuma tecla for pressionada antes do tempo de espera se esgotar.

cv2.destroyAllWindows()

    Funcionalidade: Fecha todas as janelas criadas pelo OpenCV.

    Sintaxe: cv2.destroyAllWindows()

    Parâmetros:

        Nenhum.

    Retorno:

        Nenhum.