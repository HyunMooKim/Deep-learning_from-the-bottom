{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMXf7yB3cMR96UQ8N1WgU5v",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HyunMooKim/Deep-learning_from-the-bottom/blob/main/%EB%B0%91%EB%B0%94%EB%8B%A5%EB%94%A5%EB%9F%AC%EB%8B%9D1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "<h1>밑바닥부터 시작하는 딥러닝 1 </h1>"
      ],
      "metadata": {
        "id": "rUx8wY0ClSjr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 2장 퍼셉트론\n",
        "AND, OR, NAND, XOR\n",
        "등 가장 기본적 논리구조를 표현하는 방식\n",
        "\n",
        " W.dot(x) + b 형태는 SVM 의 손실함수와 비슷한 형태\n"
      ],
      "metadata": {
        "id": "8hQxesAaj14Q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 퍼셉트론\n",
        "import numpy as np\n",
        "\n",
        "# np.array() 는 리스트를 받아서 배열로 만들어준다.\n",
        "# np.sum()은 모든 원소의 총합을 구한다.\n",
        "# 가중치 w는 각 신호의 영향력을, bias 편향력은 얼마나 쉽게 퍼셉트론이 활성화되는지를 나타낸다.\n",
        "\n",
        "def AND(x1,x2):\n",
        "  x = np.array([x1,x2])\n",
        "  w = np.array([0.5,0.5])\n",
        "  b = -0.7   # 0.5 하나론 못넘고, 두개로는 넘어야함.\n",
        "  tmp = np.sum(w*x)  + b\n",
        "  if tmp <= 0:\n",
        "    return 0\n",
        "  else:\n",
        "    return 1\n",
        "\n",
        "def NAND(x1,x2):\n",
        "  x = np.array([x1,x2])\n",
        "  w = np.array([-0.5, -0.5]) #AND에 bias와 가중치 부호 반대로 하면 된다.\n",
        "  b =  0.7\n",
        "  tmp = np.sum(w*x)  + b\n",
        "  if tmp <= 0:\n",
        "    return 0\n",
        "  else:\n",
        "    return 1\n",
        "\n",
        "def OR(x1,x2):\n",
        "  x = np.array([x1,x2])\n",
        "  w = np.array([0.5,0.5])\n",
        "  b = -0.2  #0.5 하나만으로도 넘을 수 있어야 한다.\n",
        "  tmp = np.sum(w*x)  + b\n",
        "  if tmp <= 0:\n",
        "    return 0\n",
        "  else:\n",
        "    return 1\n",
        "\n",
        "#퍼셉트론으로 XOR 게이트를 표현할 수 없다. 비선형 영역이기 때문이다. 즉,  x,y, 좌표에서 선 하나만 그어서 구분하는 문제만 가능\n",
        "#다층 퍼셉트론으로 표현한다. ]\n",
        "#NAND로 둘 다인 경우 제외, OR로 둘 다 아닌 경우 제외 이 둘을 AND로 묶어 XOR을 만들어 낸다.\n",
        "def XOR(x1,x2):\n",
        "  s1 = NAND(x1,x2)\n",
        "  s2 = OR(x1,x2)\n",
        "  y = AND(s1,s2)\n",
        "  return y\n",
        "\n",
        "print(XOR(0,0))\n",
        "print(XOR(1,0))\n",
        "print(XOR(0,1))\n",
        "print(XOR(1,1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PhNUs9Xbj456",
        "outputId": "4f67c52f-5f83-4961-f65b-4cf0da80877d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "1\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 3장 신경망\n",
        "퍼셉트론과 신경망의 차이점은, 퍼셉트론은 활성화를 0보다 크거나 작은 경우 2가지로 계단식함수를 이용.\n",
        "\n",
        "반면 신경망은 시그모이드 함수 e^x /(1 + e^x)  = 1/(1+e^-x) 를 이용 -> 로지스틱 회귀 모형\n",
        "\n",
        "\n",
        "https://gooopy.tistory.com/52"
      ],
      "metadata": {
        "id": "iTRywD3zyLtU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "x = np.array([-1.0, 1.0, 2.0])\n",
        "y = x > 0\n",
        "print(y)\n",
        "# 이렇게 배열에 대하여 부등호 연산을 하면 boolean값이 되는 점을 이용해 계단식 함수에 인자로 배열을 전달할 수 있게 개조\n",
        "\n",
        "def step_function(x):\n",
        "  return np.array(x>0, dtype=np.int )\n",
        "\n",
        "x = np.arange(-5.0, 5.0, 0.1)\n",
        "print(step_function(x))\n",
        "y = step_function(x)\n",
        "plt.plot(x,y)\n",
        "plt.ylim(-0.1,1.1)\n",
        "plt.show()\n",
        "\n",
        "\n",
        "def sigmoid(x):\n",
        "  return 1/(1+np.exp(-x))\n",
        "\n",
        "y = sigmoid(x)\n",
        "plt.plot(x,y)\n",
        "plt.ylim(-0.1,1.1)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 661
        },
        "id": "lFtHXeyMyNUB",
        "outputId": "bfd5dfab-4af2-48a7-e9d8-6050b26fc6bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[False  True  True]\n",
            "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
            " 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
            " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-22-5e9a4e0001ff>:10: DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.\n",
            "Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations\n",
            "  return np.array(x>0, dtype=np.int )\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "이렇게 매끄러워진 함수가 신경망 학습에서 아주 중요한 역할을 하게 된다.\n",
        "\n",
        "1과 0만 반환하는 계단 함수대신 소수를 반환하여 연속적인 실수가 흐르게 된다.\n",
        "\n",
        "최근에는 0이 넘으면 출력하고 0 이하면 0을 출력하는 ReLu 함수를 이용한다."
      ],
      "metadata": {
        "id": "OpjpSx4c0rla"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "def Relu(x):\n",
        "  return np.maximum(0,x)\n",
        "\n",
        "x = np.arange(-5.0, 5.0, 0.1)\n",
        "y = Relu(x)\n",
        "plt.plot(x,y)\n",
        "plt.ylim(-0.1,1.1)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "23AmjaAp1QQG",
        "outputId": "a034de17-8e18-467e-dac1-6054449a53c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 3장 행렬"
      ],
      "metadata": {
        "id": "CvDoSapc17BJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "A=np.array([[1,2,3],[4,5,6]])\n",
        "B= np.array([ [1,2],[3,4],[5,6] ])\n",
        "print('A',A)\n",
        "print()\n",
        "print('B',B)\n",
        "#차원\n",
        "print('\\n차원',np.ndim(B))\n",
        "#모양\n",
        "print('\\n모양',B.shape)\n",
        "print()\n",
        "#행렬곱\n",
        "print(np.dot(A,B))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ESaFs5Ed1-hm",
        "outputId": "dd50188f-1050-41d7-f718-a781b9c55795"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A [[1 2 3]\n",
            " [4 5 6]]\n",
            "\n",
            "B [[1 2]\n",
            " [3 4]\n",
            " [5 6]]\n",
            "\n",
            "차원 2\n",
            "\n",
            "모양 (3, 2)\n",
            "\n",
            "[[22 28]\n",
            " [49 64]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 3장 - 3층 시그모이드 신경망 구현\n",
        "\n",
        "<img src='https://ifh.cc/g/7MZLl1.jpg' border='0'></a>\n"
      ],
      "metadata": {
        "id": "Ows_9urfAnw4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "def sigmoid(x):\n",
        "  return 1/(1+np.exp(-x))\n",
        "\n",
        "def identity_function(x):\n",
        "  return x\n",
        "\n",
        "def init_network():\n",
        "  network={}\n",
        "  #0층에서 1층(노드 2개 -> 3개)\n",
        "  network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])\n",
        "  network['b1'] = np.array([0.1,0.2,0.3])\n",
        "\n",
        "  #1층에서 2층(노드3개->2개)\n",
        "  network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3, 0.6]])\n",
        "  network['b2'] = np.array([0.1,0.2])\n",
        "\n",
        "  #2층에서 3층(노드2개->2개)\n",
        "  network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])\n",
        "  network['b3'] = np.array([0.1,0.2])\n",
        "\n",
        "  return network\n",
        "\n",
        "def forward(network, x):\n",
        "  W1,W2,W3 = network['W1'], network['W2'], network['W3']\n",
        "  b1,b2,b3 = network['b1'], network['b2'], network['b3']\n",
        "\n",
        "  a1=np.dot(x,W1) +b1\n",
        "  z1 = sigmoid(a1)\n",
        "  a2=np.dot(z1,W2) +b2\n",
        "  z2 = sigmoid(a2)\n",
        "  a3 = np.dot(z2, W3) + b3\n",
        "  y = identity_function(a3)\n",
        "\n",
        "  return y\n",
        "\n",
        "network=init_network()\n",
        "x = np.array([1.0, 0.5])\n",
        "y = forward(network, x)\n",
        "print(y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "glhzs8JIArlL",
        "outputId": "b1b8aa65-5a94-4524-84b8-5700778c2b7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0.31682708 0.69627909]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Soft MAX\n",
        "세 개 이상의 class로 나뉠 경우, 각 class 에 속할 확률\n",
        "\n",
        "설명: https://wikidocs.net/35476 <- 여기 좋습니다. <br>\n",
        "      https://bookandmed.tistory.com/39"
      ],
      "metadata": {
        "id": "LwD9IgYGNhgD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "#각 점수\n",
        "a = np.array([0.3, 2.9, 4.0])\n",
        "\n",
        "#e의 x제곱\n",
        "exp_a = np.exp(a)\n",
        "\n",
        "#분모\n",
        "sum_exp_a = np.sum(exp_a)\n",
        "\n",
        "#각 클래스로 분류될 확률\n",
        "y = exp_a / sum_exp_a\n",
        "\n",
        "print(y)\n",
        "\n",
        "#함수화\n",
        "\n",
        "def softmax(a):\n",
        "  exp_a=np.exp(a)\n",
        "  sum = np.sum(exp_a)\n",
        "  y = exp_a / sum\n",
        "  return y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cQXQnixfOC64",
        "outputId": "c969beee-0ce0-4266-ebf1-6cfa4008436e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0.01821127 0.24519181 0.73659691]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 이때, e의 제곱을 이용하면 오버플로우가 발생할 수 있다.\n",
        "# 이 문제를 해결하기 위해 계산해야할 점수의 최댓값을 모든 점수에 빼주어 상대적 크기 차이만 이용할 수 있다.\n",
        "# page 93을 보면, exp() 함수 안에 상수를 더하거나 빼주어도 값이 변하지 않음을 증명한다.\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "def softmax(a):\n",
        "  c = np.max(a)\n",
        "  exp_a = np.exp(a-c) #overflow 방지\n",
        "  sum = np.sum(exp_a)\n",
        "  y = exp_a / sum\n",
        "  return y\n",
        "\n",
        "a = np.array([1010,1000,990])\n",
        "result =  softmax(a)\n",
        "print(result)\n",
        "print(np.sum(result))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "osxRif06UJ1G",
        "outputId": "fc912779-b653-4f6a-9f7d-0d93f6aadeed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[9.99954600e-01 4.53978686e-05 2.06106005e-09]\n",
            "1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 3장 손글씨 숫자 인식"
      ],
      "metadata": {
        "id": "70rzAmg-aRfK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#아래 두개 셀을 실행해 데이터 가져와야 뒤에 것들도 가능"
      ],
      "metadata": {
        "id": "3zS8xtrhu7qa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/WegraLee/deep-learning-from-scratch.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VjWOYkTAA08s",
        "outputId": "c480a8e2-029e-4497-a3f0-e8e806f8cb9f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'deep-learning-from-scratch'...\n",
            "remote: Enumerating objects: 830, done.\u001b[K\n",
            "remote: Total 830 (delta 0), reused 0 (delta 0), pack-reused 830\u001b[K\n",
            "Receiving objects: 100% (830/830), 52.21 MiB | 11.49 MiB/s, done.\n",
            "Resolving deltas: 100% (477/477), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 데이터 가져오기\n",
        "import sys, os\n",
        "from deep.dataset import mnist\n",
        "'''\n",
        "완전 처음 할 때\n",
        "1. git허브에서 가져오기\n",
        "2. sys.path에 내가 쓸 파일 추가하기\n",
        "3. 폴더 이름을 deep으로 바꾸기( - 나 from 때문에 문법오류난다)\n",
        "4. from 바꾼 폴더이름 import 내가 쓸 함수 파일이름\n",
        "'''\n",
        "# 훈련 이미지 6만장, test이미지 만장\n",
        "\n",
        "# sys.path.append('/content/deep-learning-from-scratch/dataset/mnist.py')\n",
        "# print(sys.path)\n",
        "\n",
        "\n",
        "# https://raw.githubusercontent.com/WegraLee/deep-learning-from-scratch/master/dataset/mnist.py\n",
        "# https://github.com/WegraLee/deep-learning-from-scratch.git\n",
        "\n",
        "#x_train은 이미지, t_train은 라벨\n",
        "(x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True, normalize=False)\n",
        "print(x_train.shape) #60000, 784 나오면 성공"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1YpWRb5haU-D",
        "outputId": "fa4399cd-1044-4e91-9278-ee9547abe8d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Converting train-images-idx3-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Converting train-labels-idx1-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Converting t10k-images-idx3-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Converting t10k-labels-idx1-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Creating pickle file ...\n",
            "Done!\n",
            "(60000, 784)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#이미지 열어보기\n",
        "import sys, os\n",
        "import numpy as np\n",
        "from PIL import Image\n",
        "from deep.dataset import mnist\n",
        "from matplotlib.pyplot import imshow\n",
        "\n",
        "def img_show(img):\n",
        "  pil_img = Image.fromarray(np.uint8(img))\n",
        "  imshow(pil_img)\n",
        "\n",
        "(x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True, normalize=False)\n",
        "\n",
        "img = x_train[0]\n",
        "label = t_train[0]\n",
        "print(label) #5\n",
        "\n",
        "print(img.shape) # (784, )\n",
        "img = img.reshape(28, 28)\n",
        "# 원래 이미지의 모양으로 변형 flastten=True 1차원 배열로 저장되어있기 때문에, 28*28로 다시 바꾸는 것\n",
        "print(img.shape)  #(28,28)\n",
        "\n",
        "img_show(img)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "op3OviKCBBHy",
        "outputId": "01d845ee-10fa-4b5a-dc42-ec5a3d4fcf14"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "(784,)\n",
            "(28, 28)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 신경망 구현하기\n",
        "# 28*28 크기의 이미지가 input, 0~9의 숫자가 output\n",
        "import os, sys\n",
        "import pickle\n",
        "# sys.path.append('/content/deep-learning-from-scratch/ch03/sample_weight.pkl')\n",
        "# from deep.ch03 import sample_weight 왜인지 .py와 다르게 .pkl은 이렇게 import할 수 없었다\n",
        "# 대신 실제 경로를 이용해 사용할 수 있었다. /content/deep/ch03/sample_weight.pkl\n",
        "\n",
        "from deep.dataset import mnist\n",
        "import numpy as np\n",
        "\n",
        "def sigmoid(x):\n",
        "  return 1 / (1 + np.exp(-x))\n",
        "\n",
        "def softmax(a):\n",
        "  c = np.max(a)\n",
        "  exp_a = np.exp(a-c) #overflow 방지를 위해 최대값을 다 빼준다. 결과는 변하지 않는다.\n",
        "  sum = np.sum(exp_a)\n",
        "  y = exp_a / sum\n",
        "  return y\n",
        "\n",
        "def get_data():\n",
        "  #normalize정규화(0~255의 픽셀 값을 0~1 범위로 정규화) 이걸 안하니까 sigmoid에서 runtime error발생\n",
        "  (x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True, normalize=True, one_hot_label=False) #정답만 1, 나머진 0으로 표시하는 원 핫\n",
        "  return x_test, t_test\n",
        "\n",
        "def init_network(): # 가중치와 매개변수가 주어졌다! 딕셔너리로 저장되어있는 이진파일. 최적의 가중치를 찾아내는게 딥러닝\n",
        "  with open(\"/content/deep/ch03/sample_weight.pkl\", 'rb') as f:\n",
        "    network = pickle.load(f)\n",
        "    return network\n",
        "\n",
        "#          X            W1          W2            W3          ->        Y\n",
        "#   test개수 x 784   784 x 50    50 x 100    100 x 분류개수     test개수 x 분류개수\n",
        "def predict(network,x):\n",
        "  W1, W2, W3 = network['W1'], network['W2'], network['W3']\n",
        "  b1, b2, b3 = network['b1'], network['b2'], network['b3']\n",
        "  a1 = np.dot(x, W1) + b1\n",
        "  z1 = sigmoid(a1)\n",
        "  a2 = np.dot(z1,W2) + b2\n",
        "  z2 = sigmoid(a2)\n",
        "  a3 = np.dot(z2,W3) + b3\n",
        "  y = softmax(a3)\n",
        "  return y\n",
        "\n",
        "x, t = get_data()\n",
        "network = init_network()\n",
        "\n",
        "accuracy_cnt = 0\n",
        "for i in  range(len(x)): #test는 10000개\n",
        "  y = predict(network, x[i])\n",
        "  p = np.argmax(y)  #확률이 가장 높은 인덱스 저장\n",
        "  if (p == t[i]):\n",
        "    accuracy_cnt += 1\n",
        "\n",
        "print('sigmoid 함수, softmax방식 이용한 정확도:', float(accuracy_cnt) / len(x) ) #0.9352가 나와야 정상"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ziAjVjlxD3wh",
        "outputId": "3fc5d9fd-1eea-4f94-a82a-c4675c2b7487"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sigmoid 함수, softmax방식 이용한 정확도: 0.9352\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#batch 묶음 - x[i] y[i] 에 각각 i번째 이미지와 그 결과가 저장되어 있다.\n",
        "#묶음을 이용해 계산한다. 컴퓨터는 큰 배열을 한번에 계산하는 것이 분할된 배열을 여러번 하는 것보다 빠르다.\n",
        "batch_size = 100\n",
        "accuracy_cnt = 0\n",
        "for i in range(0,len(x), batch_size):\n",
        "  x_batch = x[i:i+batch_size] # 100개의 행, 100개의 test\n",
        "  y_batch = predict(network,x_batch)\n",
        "  p = np.argmax(y_batch, axis=1 ) #100개 단위니까 열따라 이동(행으로) 100번, 최대치 index\n",
        "  accuracy_cnt +=np.sum( p == t[i:i+batch_size] )  #정답이 맞는 개수만큼 sum\n",
        "print( float(accuracy_cnt) / len(x) )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qV8vYQgG8zJb",
        "outputId": "7dad9a60-74e4-478e-e743-c7dac4575c40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.9352\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 4장 신경망 학습 - 수치 미분\n",
        "\n",
        "직선으로 분리할 수 있는 선형 분리 가능 문제는 퍼셉트론 수렴정리에 의해 유한 번의 학습을 통해 풀 수 있다.\n",
        "하지만 비선형 분리 문제는 자동으로 학습할 수 없다.<br>\n",
        "\n",
        "사람이 생각한 특징 -> 기계학습 -> 결과<br>\n",
        "딥러닝 -> 결과 (사람의 개입 최소화)<br><br>\n",
        "\n",
        "'특징'은 보통 SITF, SURF, HOG 등의 특징을 이용해 벡터로 기술하고, 이후 지도 학습 분류 기법 SVM KNN 등으로 학습할 수 있다.\n",
        "\n",
        "정확도가 아닌 손실을 지표로 하는 이유: <br>\n",
        "정확도를 지표로 삼으면 대부분의 매개변수 미분 값이 0으로, 갱신을 하기가 어려워진다. (정확도 32%라면 가중치가 조금 바뀌어도 그대로 32%일 수 있다. 반면 손실함수는 조금의 변화에도 바뀌는 연속적인 변화!)\n",
        "\n",
        "이는 계단식 함수 대신 시그모이드 같은 함수를 이용하는 이유이기도 하다."
      ],
      "metadata": {
        "id": "1PNG4mMp-01L"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 손실 측정 - 오차 제곱의 합\n",
        "import numpy as np\n",
        "#SSE 오차 제곱의 합\n",
        "def sum_squares_error(y, t):\n",
        "  return 0.5 * np.sum((y-t)**2)\n",
        "\n",
        "#정답은 2\n",
        "t= [0,0,1,0,0,0,0,0,0,0]\n",
        "\n",
        "# 2일 확률이 가장 높다고 예측\n",
        "y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]\n",
        "print('정답 2를 맞춘 경우 손실',sum_squares_error(np.array(y),np.array(t)) )\n",
        "\n",
        "# 7일 확률이 가장 높다고 예측\n",
        "y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]\n",
        "print('틀린 경우 손실', sum_squares_error(np.array(y),np.array(t)) )\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fmtdIqUZ-3WK",
        "outputId": "cd6d42f7-dae9-47be-a19d-a3e6503b7f5a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "정답 2를 맞춘 경우 손실 0.09750000000000003\n",
            "틀린 경우 손실 0.5975\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 손실 측정 - 교차 엔트로피 오차\n",
        "# 로그 씌워서 파악, 정답 인덱스의 점수가 1에 가까울 수록 0에 가까운 손실 발생\n",
        "import numpy as np\n",
        "\n",
        "# (1/N) * -시그마log(y)\n",
        "# 원핫 코딩으로 인해, 정답 인덱스가 아닌 부분은 다 0이 된다. 따라서 데이터가 하나면 추론 결과값의 -log 값이 된다.\n",
        "# 예를들어 2 가 정답이고 그 확률이 0.6인 경우 -log 0.6 이다. 값이 음수니까 앞에 - 부호를 붙여준 것.\n",
        "\n",
        "def cross_entropy_error(y,t):\n",
        "  delta = 1e-7\n",
        "  return -np.sum(t * np.log(y + delta))\n",
        "  # 아주 작은 델타를 더해줘 np.log에 0이 입력되어 -inf가 되지 않도록 함.\n",
        "\n",
        "#정답은 2\n",
        "t= [0,0,1,0,0,0,0,0,0,0]\n",
        "\n",
        "# 2일 확률이 가장 높다고 예측\n",
        "y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]\n",
        "# - (log 6 - log 10)\n",
        "print('정답 2를 맞춘 경우 손실',cross_entropy_error(np.array(y),np.array(t)) )\n",
        "\n",
        "\n",
        "# 7일 확률이 가장 높다고 예측\n",
        "y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]\n",
        "print('틀린 경우 손실', cross_entropy_error(np.array(y),np.array(t)) )\n",
        "# - (log5 - log100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uQZ_-RI1PNoF",
        "outputId": "8cc57c84-f0a0-472f-8ba8-c41603b1cc29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "정답 2를 맞춘 경우 손실 0.510825457099338\n",
            "틀린 경우 손실 2.302584092994546\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#학습 데이터 중 무작위 일부만을 이용할 수도 있다. mini-batch 학습이라고 한다.\n",
        "import numpy as np\n",
        "from deep.dataset import mnist\n",
        "(x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, one_hot_label=True)\n",
        "\n",
        "train_size = x_train.shape[0] #6만\n",
        "batch_size = 10\n",
        "# 0 이상 6만 미만의 수 중 무작위 10개 선택 ->배열로 나옴\n",
        "batch_mask = np.random.choice(train_size, batch_size)\n",
        "\n",
        "# 무작위로 뽑힌 배열을 이용해 원하는 만큼의 데이터와 정답을 가져온다.\n",
        "x_batch = x_train[batch_mask]\n",
        "t_batch = t_train[batch_mask]\n",
        "\n",
        "#이렇게 뽑은 mini-batch로 손실함수를 계산하면 적은 수를 이용할 수 있다.\n",
        "#위에서 구현한 데이터가 하나인 경우와 batch로 묶여 들어오는 경우 모두에 쓸 수 있도록\n",
        "def cross_entropy_error_mini_batch(y,t):\n",
        "  if (y.ndim ==1):\n",
        "    t = t.reshape(1,t.size)\n",
        "    y = y.reshape(1,y.size)\n",
        "  batch_size = y.shape[0]\n",
        "  # 아주 작은 델타를 더해줘 np.log에 0이 입력되어 -inf가 되지 않도록 함.\n",
        "  return -np.sum(t * np.log(y+1e-7)) / batch_size\n",
        "\n",
        "#만약 one hot incoding이 아니라 '2', '7' 등 정답 인덱스인 경우\n",
        "def cross_entropy_error_no_one_hot(y,t):\n",
        "  if (y.ndim ==1):\n",
        "    t = t.reshape(1,t.size)\n",
        "    y = y.reshape(1,y.size)\n",
        "  batch_size = y.shape[0]\n",
        "  #np.arange( 숫자 ) 는 0부터 숫자 -1 까지의 배열을 반환한다.\n",
        "  #y[np.arange(batch_size),t] 는 모든 행에 대한 정답 열을 의미한다.\n",
        "  return -np.sum(t * np.log(y[np.arange(batch_size),t]+1e-7  )) / batch_size"
      ],
      "metadata": {
        "id": "6vDuCbK3WQzv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ca9a0568-9225-4a4f-86f9-ccca85fc5b4c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Converting train-images-idx3-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Converting train-labels-idx1-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Converting t10k-images-idx3-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Converting t10k-labels-idx1-ubyte.gz to NumPy Array ...\n",
            "Done\n",
            "Creating pickle file ...\n",
            "Done!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 학습을 위한 미분\n",
        "\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "def function_1(x):\n",
        "  return 0.01*x**2 + 0.1*x\n",
        "\n",
        "def numerical_diff(f,x):\n",
        "  h = 1e-4 #10의 -4제곱! 너무 작게 하면 0으로 인식하는 문제 발생 이정도가 좋다고 알려져있다\n",
        "  return ( f(x+h) - f(x-h) ) / (2*h)    #h를 0으로 무한히 좁히는 것이 불가능하므로, x에서 앞뒤로 h만큼 이동한 실제 미분과 다른 근사치\n",
        "\n",
        "x = np.arange(0.0, 20.0, 0.1)\n",
        "y = function_1(x)\n",
        "\n",
        "plt.xlabel('x')\n",
        "plt.ylabel('y')\n",
        "plt.plot(x,y)\n",
        "plt.show()\n",
        "\n",
        "print('5에서 미분: ', numerical_diff(function_1, 5))\n",
        "print('10에서 미분: ', numerical_diff(function_1, 10) )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        },
        "id": "odeRfTAcw1e6",
        "outputId": "b5bcd344-2a37-48f1-80df-9a35e2e00935"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5에서 미분:  0.1999999999990898\n",
            "10에서 미분:  0.2999999999986347\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# gradient - 편미분 값을 벡터로 정리한 것\n",
        "# 변수 x 역시 배열 형태로 x = [x1,x2]\n",
        "def function_2(x):\n",
        "  return x[0]**2 + x[1]**2\n",
        "\n",
        "# 함수와 변수 값들을 받아 미분값 반환\n",
        "def numerical_gradient(f, x):\n",
        "  h = 1e-4\n",
        "  grad = np.zeros_like(x) #x와 형상이 같은 배열 생성\n",
        "\n",
        "  # 변수 개수 만큼 반복문이 돌아야 하는데, 한번만 도는 문제 발생.. -> return 들여쓰기 문제였음\n",
        "  for idx in range(x.size):\n",
        "    tmp_val = x[idx]\n",
        "    #각 변수에 대하여 x+h, x-h 계산\n",
        "    x[idx] = tmp_val + h\n",
        "    fxh1 = f(x)\n",
        "    x[idx] = tmp_val - h\n",
        "    fxh2 = f(x)\n",
        "\n",
        "    grad[idx] = (fxh1 - fxh2) / (2*h)\n",
        "\n",
        "    #원래 값으로 복원\n",
        "    x[idx] = tmp_val\n",
        "\n",
        "  return grad\n",
        "\n",
        "\n",
        "print('3차원(2변수 함수) 미분',numerical_gradient( function_2, np.array([3.0, 4.0]) )  )\n",
        "print('3차원(2변수 함수) 미분',numerical_gradient( function_2, np.array([0.0, 2.0]) )  )\n",
        "print('3차원(2변수 함수) 미분',numerical_gradient( function_2, np.array([3.0, 0.0]) )  )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8KD2JdCK21vU",
        "outputId": "c479ca67-482b-4ba5-ab9f-afde9f0103be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3차원(2변수 함수) 미분 [6. 8.]\n",
            "3차원(2변수 함수) 미분 [0. 4.]\n",
            "3차원(2변수 함수) 미분 [6. 0.]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "이렇게 미분값들을 구해 복잡한 함수에서 최소(혹은 최대)값을 향해 조금씩 이동하며 기울기가 0이 되는 최저점을 찾으려는 방법을 경사 하강법 이라고 한다.<br>\n",
        "그러나 실제 복잡한 현실문제에서는 안정점이 최솟값이 아닐수도 있고, 평평한 곳으로 가면서 고원(플래토)라고 하는 학습이 진행되지 않는 정체기에 빠질 수 있다."
      ],
      "metadata": {
        "id": "1DaDwmgx8A2I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 경사법으로 x1^2 + x2^2 의 최솟값 구하기\n",
        "def function_2(x):\n",
        "  return x[0]**2 + x[1]**2\n",
        "\n",
        "def gradient_descent(f, init_x, lr, step_num):\n",
        "  x = init_x\n",
        "  for i in range(step_num):\n",
        "    grad = numerical_gradient(f,x)\n",
        "    #원하는 기울기일때만 움직여야 하지 않나?\n",
        "    x = x - lr*grad\n",
        "  return x\n",
        "\n",
        "init_x = np.array([-3.0, 4.0])\n",
        "\n",
        "# 실제 최솟값 0과 아주 비슷 ! 학습률이 너무 크거나 작으면 동떨어진 값이 나온다. (너무 크게 크게 이동하며 찾기 때문)\n",
        "gradient_descent(function_2, init_x = init_x, lr= 0.1, step_num=100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pvVP_i-48eVl",
        "outputId": "b628c8a6-6e8c-491f-de90-34ab6f84a6c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([-6.11110793e-10,  8.14814391e-10])"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "학습률 처럼 사람이 직접 여러 후보 중 결정해야 하는 가중치를 hyper parameter라고 한다."
      ],
      "metadata": {
        "id": "2eg0GTUcDntn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 신경망에서의 기울기\n",
        "import numpy as np\n",
        "# !git clone 하고, deep으로 바꾸는 것 잊지 말고!\n",
        "from deep.common.functions import softmax, cross_entropy_error\n",
        "from deep.common.gradient import numerical_gradient\n",
        "\n",
        "class simpleNet:\n",
        "  def __init__(self):\n",
        "    self.W = np.random.randn(2,3) #정규 분포로 초기화\n",
        "  def predict(self, x):\n",
        "    return np.dot(x, self.W)\n",
        "  def loss(self, x, t):\n",
        "    z = self.predict(x)\n",
        "    y = softmax(z)\n",
        "    loss = cross_entropy_error(y, t)\n",
        "    return loss\n",
        "\n",
        "\n",
        "# 하나의 신경망 만들기\n",
        "net = simpleNet()\n",
        "print('created Neural Network\\n',net.W)\n",
        "\n",
        "# 초기값 설정 및 예측\n",
        "x = np.array([0.6, 0.9])\n",
        "p = net.predict(x)\n",
        "print('predict \\n',p)\n",
        "\n",
        "t = np.array([0, 0, 1]) # 정답 레이블 설정\n",
        "\n",
        "print('compare with the answer loss is: ',net.loss(x, t))\n",
        "\n",
        "\n",
        "# 함수를 손실함수로 정의\n",
        "def f(W):\n",
        "  return net.loss(x,t)\n",
        "# f = lambda w: net.loss(x,t) 로도 가능\n",
        "\n",
        "# 함수와 값을 받아 미분\n",
        "dW = numerical_gradient(f, net.W)\n",
        "print(dW)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j1p_B1RB0FUI",
        "outputId": "3098febc-3056-4d96-f52b-4ca3ff1e2977"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "created Neural Network\n",
            " [[ 0.66000002  0.54932187 -2.37743454]\n",
            " [ 0.57481429  0.3864953   1.51500164]]\n",
            "predict \n",
            " [ 0.91333288  0.67743889 -0.06295925]\n",
            "compare with the answer loss is:  1.749436680490603\n",
            "[[ 0.27693531  0.21874135 -0.49567666]\n",
            " [ 0.41540297  0.32811202 -0.74351499]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "딥러닝 프레임워크 중 SGD (stochastic gradient descent) 방법이 있다.\n",
        "이는\n",
        "\n",
        "1. 미니배치 무작위 선택\n",
        "2. 기울기 산출\n",
        "3. 매개 변수 갱신\n",
        "\n",
        "의 3단계를 반복하는 함수이다.\n",
        "즉, 복잡한 매개변수 공간에서(아주 큰 n차원) 기울어진 방향으로 매개변수 값을 갱신하는 일을 몇 번이고 반복하는 단순한 방법."
      ],
      "metadata": {
        "id": "tHWdGU1m6olO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#2층 신경망 클래스 구현\n",
        "import numpy as np\n",
        "# !git clone 하고, deep으로 바꾸는 것 잊지 말고!\n",
        "from deep.common.functions import softmax, cross_entropy_error\n",
        "from deep.common.gradient import numerical_gradient\n",
        "from deep.dataset.mnist import load_mnist\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "def sigmoid(x):\n",
        "  return 1/(1+np.exp(-x))\n",
        "\n",
        "\n",
        "# 0층 input -> 1층 hidden -> 2층 output\n",
        "class TwoLayerNet:\n",
        "  def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):\n",
        "  # 가중치 초기화 , 정규분포를 따르는 난수로 가중치 초기화, 0으로 편향 초기화\n",
        "    self.params = {} #create a dictionary\n",
        "    self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)\n",
        "    self.params['b1'] = np.zeros(hidden_size)\n",
        "    self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)\n",
        "    self.params['b2'] = np.zeros(output_size)\n",
        "\n",
        "  def predict(self, x):\n",
        "    W1, W2 = self.params['W1'], self.params['W2']\n",
        "    b1, b2 = self.params['b1'], self.params['b2']\n",
        "    a1 = np.dot(x, W1) + b1\n",
        "    z1 = sigmoid(a1)\n",
        "    a2 = np.dot(z1, W2) + b2\n",
        "    y = softmax(a2)\n",
        "    return y\n",
        "\n",
        "\n",
        "    # x:입력 데이터, t:정답 레이블\n",
        "  def loss(self, x, t):\n",
        "    y = self.predict(x)\n",
        "    return cross_entropy_error(y, t)\n",
        "\n",
        "  def accuracy(self, x, t):\n",
        "    y = self.predict(x)\n",
        "    y = np.argmax(y, axis=1)\n",
        "    t = np.argmax(t, axis=1)\n",
        "\n",
        "    accuracy = np.sum(y == t) / float(x.shape[0])\n",
        "    return accuracy\n",
        "\n",
        "    # x : 입력 데이터, t : 정답 레이블\n",
        "  def numerical_gradient(self, x, t):\n",
        "    loss_W = lambda W: self.loss(x, t)\n",
        "\n",
        "    grads = {}\n",
        "    grads['W1'] = numerical_gradient(loss_W, self.params['W1'])\n",
        "    grads['b1'] = numerical_gradient(loss_W, self.params['b1'])\n",
        "    grads['W2'] = numerical_gradient(loss_W, self.params['W2'])\n",
        "    grads['b2'] = numerical_gradient(loss_W, self.params['b2'])\n",
        "\n",
        "    return grads\n",
        "\n",
        "    '''\n",
        "    def gradient(self, x, t):\n",
        "        W1, W2 = self.params['W1'], self.params['W2']\n",
        "        b1, b2 = self.params['b1'], self.params['b2']\n",
        "        grads = {}\n",
        "\n",
        "        batch_num = x.shape[0]\n",
        "\n",
        "        # forward\n",
        "        a1 = np.dot(x, W1) + b1\n",
        "        z1 = sigmoid(a1)\n",
        "        a2 = np.dot(z1, W2) + b2\n",
        "        y = softmax(a2)\n",
        "\n",
        "        # backward\n",
        "        dy = (y - t) / batch_num\n",
        "        grads['W2'] = np.dot(z1.T, dy)\n",
        "        grads['b2'] = np.sum(dy, axis=0)\n",
        "\n",
        "        da1 = np.dot(dy, W2.T)\n",
        "        dz1 = sigmoid_grad(a1) * da1\n",
        "        grads['W1'] = np.dot(x.T, dz1)\n",
        "        grads['b1'] = np.sum(dz1, axis=0)\n",
        "\n",
        "        return grads\n",
        "   '''\n",
        "\n",
        "\n",
        "# 미니배치 학습 구현\n",
        "(x_train, t_trian), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True )\n",
        "\n",
        "train_loss_list = []\n",
        "\n",
        "# hyper parameter\n",
        "iters_num = 10\n",
        "train_size = x_train.shape[0]\n",
        "batch_size = 100\n",
        "learning_rate = 0.1\n",
        "\n",
        "#input 이미지(28*28) ouput 0~9 숫자\n",
        "network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)\n",
        "\n",
        "for i in range(iters_num):\n",
        "  print(i)\n",
        "  # mini batch   0~60000 중 100개\n",
        "  batch_mask = np.random.choice(train_size, batch_size)\n",
        "  x_batch = x_train[batch_mask]\n",
        "  t_batch = t_train[batch_mask]\n",
        "  # 기울기 계산\n",
        "  grad = network.numerical_gradient(x_batch, t_batch)\n",
        "\n",
        "\n",
        "  # 매개변수 갱신\n",
        "  for key in ('W1', 'b1', 'W2', 'b2'):\n",
        "    network.params[key] -= learning_rate * grad[key]\n",
        "\n",
        "  #학습 기록\n",
        "  loss = network.loss(x_batch, t_batch)\n",
        "  train_loss_list.append(loss)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CBew-7S9679I",
        "outputId": "b0def494-41b1-4714-af5b-2d588f055c31"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#학습이 진행됨에 따라 손실이 줄었을까?\n",
        "#100 번하고 싶지만, 너무 오래걸린다.\n",
        "print(train_loss_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ilJ5xkWfvli7",
        "outputId": "6247abd1-6aca-4d84-f17d-6180beb10336"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2.2925339361755603, 2.297691859885353, 2.292977378646004, 2.2921516495310588, 2.2714990688594807, 2.292138527937061, 2.3081221835024244, 2.298603896867228, 2.2930658991085537, 2.2746945609797176]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "# 손실이 줄었는지 확인  - 안 줄었다??\n",
        "# 1바퀴에 1분 걸려서 더 못하겠다.\n",
        "# 알고 보니 뒤에 나오는 오차역전파법이 훨씬 빠르다. 책에서도 그 방법을 이용해 그림을 그렸을듯.\n",
        "plt.plot( range(1,iters_num+1)  , train_loss_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        },
        "id": "iFZrjyp3FQTk",
        "outputId": "5f3e7e5f-1998-43d2-bede-d53cac39f919"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f1e3af2b220>]"
            ]
          },
          "metadata": {},
          "execution_count": 25
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# epoch - 훈련 데이터만큼 학습 했을 때의 단위이다.\n",
        "# 즉, 6만 개 사진을 100 미니배치씩 했다면, 600회가 1에폭이다.\n",
        "# 과적합을 막기 위해, 1 epoch이 될때마다 test데이터와 train데이터 정확도를 비교하여 과적합 발생 시점을 찾을 수 있다.\n",
        "\n",
        "#위의 코드와 달라진 점만 보면 된다.\n",
        "\n",
        "import numpy as np\n",
        "# !git clone 하고, deep으로 바꾸는 것 잊지 말고!\n",
        "from deep.common.functions import softmax, cross_entropy_error, sigmoid\n",
        "from deep.common.gradient import numerical_gradient\n",
        "from deep.dataset.mnist import load_mnist\n",
        "\n",
        "class TwoLayerNet:\n",
        "  def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):\n",
        "    self.params = {} #create a dictionary\n",
        "    self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)\n",
        "    self.params['b1'] = np.zeros(hidden_size)\n",
        "    self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)\n",
        "    self.params['b2'] = np.zeros(output_size)\n",
        "\n",
        "  def predict(self, x):\n",
        "    W1, W2 = self.params['W1'], self.params['W2']\n",
        "    b1, b2 = self.params['b1'], self.params['b2']\n",
        "    a1 = np.dot(x, W1) + b1\n",
        "    z1 = sigmoid(a1)\n",
        "    a2 = np.dot(z1, W2) + b2\n",
        "    y = softmax(a2)\n",
        "    return y\n",
        "\n",
        "  def loss(self, x, t):\n",
        "    y = self.predict(x)\n",
        "    return cross_entropy_error(y, t)\n",
        "\n",
        "  def accuracy(self, x, t):\n",
        "    y = self.predict(x)\n",
        "    y = np.argmax(y, axis=1)\n",
        "    t = np.argmax(t, axis=1)\n",
        "\n",
        "    accuracy = np.sum(y == t) / float(x.shape[0])\n",
        "    return accuracy\n",
        "  def numerical_gradient(self, x, t):\n",
        "    loss_W = lambda W: self.loss(x, t)\n",
        "\n",
        "    grads = {}\n",
        "    grads['W1'] = numerical_gradient(loss_W, self.params['W1'])\n",
        "    grads['b1'] = numerical_gradient(loss_W, self.params['b1'])\n",
        "    grads['W2'] = numerical_gradient(loss_W, self.params['W2'])\n",
        "    grads['b2'] = numerical_gradient(loss_W, self.params['b2'])\n",
        "\n",
        "    return grads\n",
        "\n",
        "\n",
        "(x_train, t_trian), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True )\n",
        "train_loss_list = []\n",
        "\n",
        "iters_num = 10\n",
        "train_size = x_train.shape[0]\n",
        "batch_size = 100\n",
        "learning_rate = 0.1\n",
        "\n",
        "network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)\n",
        "\n",
        "##########################달라진곳############################\n",
        "train_acc_list = []\n",
        "test_acc_list = []\n",
        "iter_per_epoch = max(train_size / batch_size, 1)\n",
        "##########################-----############################\n",
        "\n",
        "for i in range(iters_num):\n",
        "  print(i,'번째 학습중')\n",
        "  # mini batch   0~60000 중 100개\n",
        "  batch_mask = np.random.choice(train_size, batch_size)\n",
        "  x_batch = x_train[batch_mask]\n",
        "  t_batch = t_train[batch_mask]\n",
        "  # 기울기 계산\n",
        "  grad = network.numerical_gradient(x_batch, t_batch)\n",
        "\n",
        "  # 매개변수 갱신\n",
        "  for key in ('W1', 'b1', 'W2', 'b2'):\n",
        "    network.params[key] -= learning_rate * grad[key]\n",
        "\n",
        "  #학습 기록\n",
        "  loss = network.loss(x_batch, t_batch)\n",
        "  train_loss_list.append(loss)\n",
        "\n",
        "  ##########################달라진곳############################\n",
        "  if i % iter_per_epoch == 0:\n",
        "    train_acc = network.accuracy(x_train, t_train)\n",
        "    test_acc = network.accuracy(x_test, t_test)\n",
        "    train_acc_list.append(train_acc)\n",
        "    test_acc_list.append(test_acc)\n",
        "    print(\"train acc, test acc | \" + str(train_acc) +\",\" + str(test_acc) )\n",
        "  ##########################-----############################\n",
        "  # 너무 오래 걸리는 관계로...."
      ],
      "metadata": {
        "id": "uy26lG03NlZb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a26e4814-7221-491f-d7fe-9510e5a8ac1e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 번째 학습중\n",
            "train acc, test acc | 0.10441666666666667,0.1028\n",
            "1 번째 학습중\n",
            "2 번째 학습중\n",
            "3 번째 학습중\n",
            "4 번째 학습중\n",
            "5 번째 학습중\n",
            "6 번째 학습중\n",
            "7 번째 학습중\n",
            "8 번째 학습중\n",
            "9 번째 학습중\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#5장 신경망학습 - 오차역전파법  backward propagation\n",
        "<br>cs231n에 나오는 계산 그래프와 연쇄법칙!\n",
        "chain rule을 이용해 미분을 빠르게 만들어준다.\n",
        "위의 방법은 100개 mini-batch를 미분해 갱신하는 데에 1분이 걸렸다."
      ],
      "metadata": {
        "id": "Hs_M1fVDaOzH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/WegraLee/deep-learning-from-scratch.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DMed0U1BuLb2",
        "outputId": "3bc4aa69-aa85-41b0-a7e0-695025ddc1f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'deep-learning-from-scratch'...\n",
            "remote: Enumerating objects: 826, done.\u001b[K\n",
            "remote: Total 826 (delta 0), reused 0 (delta 0), pack-reused 826\u001b[K\n",
            "Receiving objects: 100% (826/826), 52.21 MiB | 19.92 MiB/s, done.\n",
            "Resolving deltas: 100% (477/477), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 아주 간단한 사과 구매 계산 그래프 = P * Q * T\n",
        "# 곱셈 Layer\n",
        "class MulLayer:\n",
        "  #self.x,  self.y 는 각 노드마다 따로 만들게 된다.\n",
        "  def __init__(self):\n",
        "    self.x = None\n",
        "    self.y = None\n",
        "  def forward(self, x, y):\n",
        "    self.x = x\n",
        "    self.y = y\n",
        "    out = x * y\n",
        "    return out\n",
        "  # 단순 곱셈이므로 서로가 미분값이 된다.\n",
        "  def backward(self, dout):\n",
        "    dx = dout * self.y\n",
        "    dy = dout * self.x\n",
        "    return dx,dy\n",
        "P = 100\n",
        "Q = 2\n",
        "T = 1.1\n",
        "\n",
        "#계층들\n",
        "mul_apple_layer = MulLayer()\n",
        "mul_tax_layer = MulLayer()\n",
        "\n",
        "#순전파\n",
        "PQ = mul_apple_layer.forward(P,Q)\n",
        "Total_Cost = mul_tax_layer.forward(PQ, T)\n",
        "\n",
        "print(Total_Cost)\n",
        "\n",
        "#역전파\n",
        "#첫 시작은 1로 두 곱셈이 서로 미분값, 그 후로는 chain처럼 계속 곱해나간다.\n",
        "dTotal_Cost = 1\n",
        "dPQ, dT = mul_tax_layer.backward(dTotal_Cost)\n",
        "dP, dQ = mul_apple_layer.backward(dPQ)\n",
        "print(dP,dQ,dT)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pWsHkZHjaupc",
        "outputId": "79ddc906-e4a3-45f1-868c-213e362580b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "220.00000000000003\n",
            "2.2 110.00000000000001 200\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# sigmoid 노드 구현\n",
        "import numpy as np\n",
        "\n",
        "class Sigmoid:\n",
        "  def __init__(self):\n",
        "    self.out = None\n",
        "\n",
        "  def forward(self, x):\n",
        "    out = 1 / (1 + np.exp(-x))\n",
        "    self.out = out\n",
        "    return out\n",
        "\n",
        " # page 167 ~ 170에 왜 시그모이드의 편미분 chain이 y(1-y) 가 되는지 나온다.\n",
        "  def backward(self, dout):\n",
        "    dx = dout * (1.0 - self.out) * self.out\n",
        "    return dx"
      ],
      "metadata": {
        "id": "UC7nSC-jjkpO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#affine 구현\n",
        "#위에서 한 계산 그래프를 행렬 단위로 진행.\n",
        "# common.layers.py에 있는 affine함수 구현은 4차원 데이터까지 가능한 버전\n",
        "\n",
        "class Affine:\n",
        "  def __init__(self,W,b):\n",
        "    self.W = W\n",
        "    self.b = b\n",
        "    self.x = None\n",
        "    self.dw = None\n",
        "    self.db = None\n",
        "  def forward(self,x):\n",
        "    self.x=x\n",
        "    out = np.dot(x, self.W) + self.b\n",
        "    return out\n",
        "  #스칼라는 아니지만, 어쨋든 곱셈이므로 결국 곱한 상대가 미분값\n",
        "  def backward(self, dout):\n",
        "    dx = np.dot(dout,self.W.T)\n",
        "    self.dW = np.dot(self.x.T, dout)\n",
        "    #편향은 상수아닌가? 미분값이 있나?\n",
        "    self.db = np.sum(dout,axis=0)\n",
        "    return dx"
      ],
      "metadata": {
        "id": "rE1v3Xhqg-PI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# soft max with loss 노드 구현\n",
        "\n",
        "def softmax(x):\n",
        "    if x.ndim == 2:\n",
        "        x = x.T\n",
        "        x = x - np.max(x, axis=0)\n",
        "        y = np.exp(x) / np.sum(np.exp(x), axis=0)\n",
        "        return y.T\n",
        "\n",
        "    x = x - np.max(x) # 오버플로 대책\n",
        "    return np.exp(x) / np.sum(np.exp(x))\n",
        "\n",
        "\n",
        "def cross_entropy_error(y, t):\n",
        "    if y.ndim == 1:\n",
        "        t = t.reshape(1, t.size)\n",
        "        y = y.reshape(1, y.size)\n",
        "\n",
        "    # 훈련 데이터가 원-핫 벡터라면 정답 레이블의 인덱스로 반환\n",
        "    if t.size == y.size:\n",
        "        t = t.argmax(axis=1)\n",
        "\n",
        "    batch_size = y.shape[0]\n",
        "    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size\n",
        "\n",
        "\n",
        "class SoftmaxWithLoss:\n",
        "  def __init__(self):\n",
        "    self.loss = None #loss\n",
        "    self.y = None  #softmax 의 출력\n",
        "    self.t = None  #정답 label(one-hot vector)\n",
        "\n",
        "  def forward(self, x, t):\n",
        "    self.t = t\n",
        "    self.y = softmax(x)\n",
        "    self.loss = cross_entropy_error(self.y, self.t)\n",
        "    return self.loss\n",
        "\n",
        "  def backward(self, dout=1):\n",
        "    batch_size = self.t.shape[0]\n",
        "    dx = (self.y - self.t) / batch_size\n",
        "    return dx\n",
        "\n"
      ],
      "metadata": {
        "id": "A1NtlzQMnnko"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 오차역전파법을 적용한 신경망 구현\n",
        "\n",
        "import numpy as np\n",
        "from deep.common.gradient import numerical_gradient\n",
        "# layer.py에 가서 common 앞에 deep넣어주어야함.\n",
        "from deep.common.layers import *\n",
        "from collections import OrderedDict\n",
        "\n",
        "class TwoLayerNet:\n",
        "\n",
        "  def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):\n",
        "    self.params = {} #create a dictionary\n",
        "    self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)\n",
        "    self.params['b1'] = np.zeros(hidden_size)\n",
        "    self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)\n",
        "    self.params['b2'] = np.zeros(output_size)\n",
        "\n",
        "  #계층생성 - 순서가 있는 딕셔너리를 이용, 순전파는 순서대로 역전파는 반대로\n",
        "    self.layers = OrderedDict()\n",
        "    self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])\n",
        "    self.layers['Relu1'] = Relu()\n",
        "    self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])\n",
        "\n",
        "    self.lastLayer = SoftmaxWithLoss()\n",
        "\n",
        "  def predict(self, x):\n",
        "    for layer in self.layers.values():\n",
        "      x = layer.forward(x)\n",
        "    return x\n",
        "\n",
        "  def loss(self, x,t):\n",
        "    y = self.predict()\n",
        "    return self.lastLayer.forward(y,t)\n",
        "\n",
        "  def accuracy(self, x, t):\n",
        "    y = self.predict(x)\n",
        "    y = np.argmax(y, axis=1)\n",
        "    #one hot vector라면 1을 정답 인덱스로\n",
        "    if t.ndim != 1 : t = np.argmax(t, axis = 1 )\n",
        "\n",
        "    accuracy = np.sum(y==t) / float(x.shape[0])\n",
        "    return accuracy\n",
        "\n",
        "  def gradient(self, x,t ):\n",
        "    #순전파\n",
        "    self.loss(x,t)\n",
        "\n",
        "    #역전파\n",
        "    dout=1\n",
        "    dout = self.lastLayer.backward(dout)\n",
        "\n",
        "    layers=list(self.layers.values())\n",
        "    layers.reverse()\n",
        "    for layer in layers:\n",
        "      dout=layer.backward(dout)\n",
        "    #result\n",
        "    grads = {}\n",
        "    grads['W1'] = self.layers['Affine1'].dW\n",
        "    grads['b1'] = self.layers['Affine1'].db\n",
        "    grads['W2'] = self.layers['Affine2'].dW\n",
        "    grads['b2'] = self.layers['Affine2'].db\n",
        "\n",
        "    return grads\n",
        ""
      ],
      "metadata": {
        "id": "1byvqUsoqmlS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#먼저 했던 수치 미분과 나중해 했던 오차역전파법 중\n",
        "# 구현이 쉽지만 더 느린 수치 미분은 오차역전파법이 제대로 되었는지 확인할 때 쓰인다.\n",
        "# 바로 위 코드 돌리고 돌려야함\n",
        "from deep.dataset.mnist import load_mnist\n",
        "from deep.ch05.two_layer_net import TwoLayerNet\n",
        "\n",
        "(x_train, t_trian), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True )\n",
        "\n",
        "network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)\n",
        "\n",
        "x_batch = x_train[:3]\n",
        "t_batch = t_trian[:3]\n",
        "\n",
        "grad_numerical = network.numerical_gradient(x_batch, t_batch)\n",
        "grad_backprop = network.gradient(x_batch, t_batch)\n",
        "\n",
        "for key in grad_numerical.keys():\n",
        "  diff = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )\n",
        "  print(key + \":\" + str(diff))\n",
        "# 아주 작은 오차면 성공!"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R-UxozAtxqBm",
        "outputId": "7cafaf6d-e639-4359-fb9f-ec64513b5530"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "W1:4.77772187953562e-10\n",
            "b1:2.9894537577492648e-09\n",
            "W2:6.546715693493958e-09\n",
            "b2:1.3924283003008409e-07\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 오류가 없었다면, 이제 신경망 학습을 수치 미분이 아니라 오차역전법으로 진행해보자.\n",
        "# 수치 미분은 아주 오래 걸렸던 것을 기억하라!\n",
        "from deep.dataset.mnist import load_mnist\n",
        "from deep.ch05.two_layer_net import TwoLayerNet\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "(x_train, t_trian), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True )\n",
        "train_loss_list = []\n",
        "\n",
        "iters_num = 1000\n",
        "train_size = x_train.shape[0]\n",
        "batch_size = 100\n",
        "learning_rate = 0.1\n",
        "\n",
        "train_acc_list = []\n",
        "test_acc_list = []\n",
        "iter_per_epoch = max(train_size / batch_size, 1)\n",
        "\n",
        "network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)\n",
        "\n",
        "for i in range(iters_num):\n",
        "  # mini batch   0~60000 중 100개\n",
        "  batch_mask = np.random.choice(train_size, batch_size)\n",
        "  x_batch = x_train[batch_mask]\n",
        "  t_batch = t_train[batch_mask]\n",
        "  ###############4장과 달라진 곳#######################\n",
        "  # grad = network.numerical_gradient(x_batch, t_batch)\n",
        "  grad = network.gradient(x_batch, t_batch)\n",
        "\n",
        "  # 매개변수 갱신\n",
        "  for key in ('W1', 'b1', 'W2', 'b2'):\n",
        "    network.params[key] -= learning_rate * grad[key]\n",
        "\n",
        "  #학습 기록\n",
        "  loss = network.loss(x_batch, t_batch)\n",
        "  train_loss_list.append(loss)\n",
        "\n",
        "  if i % iter_per_epoch == 0:\n",
        "    train_acc = network.accuracy(x_train, t_train)\n",
        "    test_acc = network.accuracy(x_test, t_test)\n",
        "    train_acc_list.append(train_acc)\n",
        "    test_acc_list.append(test_acc)\n",
        "    print(\"train acc, test acc | \" + str(train_acc) +\",\" + str(test_acc) )\n",
        "\n",
        "#train acc 와 test acc가 차이가 많이 나면 과적합!"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RJy7CAuuz8Ho",
        "outputId": "a0e722de-308c-4a7b-f738-8dede4e77682"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "train acc, test acc | 0.08555,0.0851\n",
            "train acc, test acc | 0.9023833333333333,0.9069\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "# 손실이 줄었는지 확인이 된다!\n",
        "plt.plot( range(1,iters_num+1)  , train_loss_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        },
        "id": "JcCk4z_Z1lJR",
        "outputId": "aa7bd2a1-a589-47b6-aa0a-bd87c0b04d57"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f0db7139c40>]"
            ]
          },
          "metadata": {},
          "execution_count": 35
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#6장 학습 관련 기술들"
      ],
      "metadata": {
        "id": "JReknB7JLt2r"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<h4>최적화 방법</h4>\n",
        "1. 기울기를 계속 갱신하며 최적점을 찾아가는 SDG\n",
        "<br>-단순한 방법\n",
        "<br>-가장 가파른 기울기가 가르키는 방향이 최적점과 먼 경우 비효율적\n",
        "<br><br>\n",
        "2. momentum 운동량\n",
        "<br>-이전 갱신의 velocity를 구해 momentum을 곱하여 학습에 더해준다..(첫 V는 0)\n",
        "<br>- V = momentum * (이전 V) - learning rate * grad\n",
        "<br>+ 기울기는 V에 - , -기울기는 V에 +\n",
        "따라서 같은 방향으로 계속 움직이면 일정하게 가속하고, 지그재그 움직임은 가속도가 일정하지 않게 된다. page 196에 더 효율적인 경우가 나온다.\n",
        "<br><br>\n",
        "3. AdaGrad\n",
        "<br>-매개변수가 갱신되어 감에 따라 학습률을 감소 시킨다.\n",
        "<br>-더 많이 갱신될 수록 더 많이 감소\n",
        "<br><br>\n",
        "4. Adam - momentum + AdaGrad\n",
        "<br><br>\n",
        "모든 상황에 맞는 뛰어난 기법이란 없다. 상황에 맞게 써야 한다."
      ],
      "metadata": {
        "id": "l9RzUqPGLxWR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<h4>가중치 초기값으로 인한 기울기 소실문제:</h4>\n",
        "<bt>\n",
        "<br>초기값이 너무 크면 시그모이드 함수의 출력이 0과 1에 가까워질 때 그 미분은 0에 다가간다. 따라서 데이터가 0과 1에 치우쳐 분포하게 되면 기울기가 점점 작아지다가 사라진다. 층을 깊게 하는 딥러닝일수록 더 심각한 문제가 될 수 있다.\n",
        "<br>\n",
        "1. ReLU 를 이용할 때는, He초깃값을\n",
        "<br>\n",
        "2. sigmoid나 tanh 등 S자 모양 곡선일 때는 Xavier를 초깃값으로 하는 것이 모범사례\n",
        "<br>\n",
        "3. batch noramization을 이용할 수도 있다.\n",
        "<br> mini batch 입력데이터를 평균0, 분산 1 인 정규분포로 정규화하여 데이터가 덜 치우지게 만드는 방법.\n"
      ],
      "metadata": {
        "id": "KGaCGplyhTIo"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<h4>Over Fitting</h4>\n",
        "<br>매게 변수가 많고 복잡한 모델이나 훈련 데이터가 적은 경우 발생 가능\n",
        "<br>\n",
        "1. 가중치 감소 방법: W절댓값의 합, 제곱합의 루트 등 정규화 항을 손실 함수에 더하여 과적합 방지. 1/2 入 W^2\n",
        "2. dropout: 훈련 때 무작위로 노드를 삭제하여 학습하고 test 때는 모든 뉴런에 신호를 전달한다. 단, test 시 각 뉴런의 출력에 훈련 때 삭제 안 한 비율을 곱하여 출력한다."
      ],
      "metadata": {
        "id": "HVPwv6onlyKe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<h4>data 나누기</h4>\n",
        "1. 훈련 데이터: 매개변수 학습\n",
        "<br>2. 검증 데이터: 하이퍼파라미터 성능 평가\n",
        "<br>3. 시험 데이터: 신경망의 범용 성능 평가"
      ],
      "metadata": {
        "id": "Ydh8gcxhpwHO"
      }
    }
  ]
}