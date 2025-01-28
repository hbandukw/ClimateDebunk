
Time
#
Log Message
12.9s	0	Collecting nlpaug
12.9s	1	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	2	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	3	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	4	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	5	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	6	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	7	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	8	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	9	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	10	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	11	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	12	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	13	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	14	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	15	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	16	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	17	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	18	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	19	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	20	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	21	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	22	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	23	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	24	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	25	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	26	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	27	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	28	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	29	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	30	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	31	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	32	[?25hInstalling collected packages: nlpaug
16.8s	33	Successfully installed nlpaug-1.1.11
17.7s	34	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	35	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	36	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	37	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	38	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	39	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	40	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	41	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	42	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	43	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	44	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	45	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	46	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	47	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	48	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	49	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	50	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	51	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	52	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	53	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	54	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	55	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	56	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
39.5s	57	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	58	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	59	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
12.9s	60	Collecting nlpaug
12.9s	61	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	62	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	63	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	64	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	65	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	66	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	67	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	68	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	69	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	70	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	71	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	72	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	73	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	74	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	75	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	76	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	77	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	78	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	79	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	80	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	81	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	82	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	83	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	84	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	85	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	86	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	87	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	88	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	89	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	90	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	91	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	92	[?25hInstalling collected packages: nlpaug
16.8s	93	Successfully installed nlpaug-1.1.11
17.7s	94	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	95	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	96	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	97	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	98	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	99	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	100	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	101	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	102	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	103	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	104	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	105	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	106	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	107	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	108	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	109	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	110	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	111	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	112	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	113	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	114	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	115	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	116	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
39.5s	117	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	118	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	119	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
12.9s	120	Collecting nlpaug
12.9s	121	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	122	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	123	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	124	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	125	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	126	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	127	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	128	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	129	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	130	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	131	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	132	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	133	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	134	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	135	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	136	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	137	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	138	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	139	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	140	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	141	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	142	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	143	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	144	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	145	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	146	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	147	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	148	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	149	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	150	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	151	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	152	[?25hInstalling collected packages: nlpaug
16.8s	153	Successfully installed nlpaug-1.1.11
17.7s	154	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	155	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	156	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	157	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	158	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	159	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	160	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	161	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	162	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	163	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	164	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	165	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	166	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	167	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	168	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	169	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	170	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	171	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	172	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	173	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	174	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	175	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	176	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	177	Using device: cuda
39.5s	178	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	179	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	180	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	181	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	182	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	183	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	184	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	185	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
12.9s	186	Collecting nlpaug
12.9s	187	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	188	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	189	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	190	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	191	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	192	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	193	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	194	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	195	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	196	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	197	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	198	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	199	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	200	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	201	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	202	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	203	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	204	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	205	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	206	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	207	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	208	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	209	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	210	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	211	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	212	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	213	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	214	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	215	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	216	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	217	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	218	[?25hInstalling collected packages: nlpaug
16.8s	219	Successfully installed nlpaug-1.1.11
17.7s	220	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	221	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	222	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	223	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	224	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	225	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	226	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	227	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	228	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	229	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	230	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	231	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	232	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	233	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	234	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	235	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	236	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	237	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	238	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	239	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	240	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	241	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	242	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	243	Using device: cuda
6093.7s	244	Stopping early at epoch 9
39.5s	245	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	246	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	247	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	248	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	249	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	250	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	251	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	252	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	253	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	254	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	255	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	256	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	257	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	258	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	259	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
12.9s	260	Collecting nlpaug
12.9s	261	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	262	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	263	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	264	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	265	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	266	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	267	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	268	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	269	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	270	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	271	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	272	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	273	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	274	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	275	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	276	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	277	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	278	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	279	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	280	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	281	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	282	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	283	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	284	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	285	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	286	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	287	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	288	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	289	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	290	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	291	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	292	[?25hInstalling collected packages: nlpaug
16.8s	293	Successfully installed nlpaug-1.1.11
17.7s	294	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	295	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	296	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	297	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	298	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	299	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	300	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	301	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	302	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	303	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	304	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	305	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	306	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	307	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	308	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	309	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	310	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	311	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	312	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	313	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	314	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	315	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	316	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	317	Using device: cuda
6093.7s	318	Stopping early at epoch 9
39.5s	319	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	320	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	321	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	322	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	323	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	324	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	325	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	326	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	327	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	328	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	329	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	330	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	331	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	332	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	333	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
12.9s	334	Collecting nlpaug
12.9s	335	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	336	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	337	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	338	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	339	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	340	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	341	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	342	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	343	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	344	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	345	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	346	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	347	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	348	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	349	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	350	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	351	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	352	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	353	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	354	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	355	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	356	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	357	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	358	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	359	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	360	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	361	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	362	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	363	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	364	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	365	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	366	[?25hInstalling collected packages: nlpaug
16.8s	367	Successfully installed nlpaug-1.1.11
17.7s	368	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	369	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	370	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	371	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	372	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	373	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	374	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	375	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	376	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	377	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	378	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	379	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	380	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	381	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	382	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	383	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	384	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	385	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	386	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	387	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	388	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	389	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	390	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	391	Using device: cuda
6093.7s	392	Stopping early at epoch 9
39.5s	393	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	394	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	395	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	396	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	397	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	398	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	399	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	400	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	401	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	402	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	403	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	404	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	405	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	406	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	407	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	408	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
12.9s	409	Collecting nlpaug
12.9s	410	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	411	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	412	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	413	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	414	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	415	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	416	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	417	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	418	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	419	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	420	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	421	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	422	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	423	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	424	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	425	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	426	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	427	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	428	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	429	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	430	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	431	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	432	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	433	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	434	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	435	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	436	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	437	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	438	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	439	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	440	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	441	[?25hInstalling collected packages: nlpaug
16.8s	442	Successfully installed nlpaug-1.1.11
17.7s	443	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	444	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	445	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	446	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	447	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	448	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	449	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	450	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	451	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	452	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	453	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	454	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	455	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	456	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	457	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	458	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	459	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	460	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	461	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	462	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	463	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	464	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	465	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	466	Using device: cuda
6093.7s	467	Stopping early at epoch 9
39.5s	468	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	469	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	470	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	471	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	472	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	473	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	474	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	475	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	476	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	477	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	478	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	479	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	480	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	481	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	482	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	483	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
12.9s	484	Collecting nlpaug
12.9s	485	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	486	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	487	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	488	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	489	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	490	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	491	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	492	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	493	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	494	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	495	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	496	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	497	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	498	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	499	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	500	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	501	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	502	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	503	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	504	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	505	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	506	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	507	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	508	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	509	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	510	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	511	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	512	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	513	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	514	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	515	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	516	[?25hInstalling collected packages: nlpaug
16.8s	517	Successfully installed nlpaug-1.1.11
17.7s	518	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	519	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	520	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	521	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	522	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	523	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	524	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	525	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	526	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	527	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	528	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	529	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	530	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	531	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	532	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	533	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	534	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	535	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	536	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	537	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	538	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	539	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	540	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	541	Using device: cuda
6093.7s	542	Stopping early at epoch 9
16050.3s	543	Stopping early at epoch 10
39.5s	544	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	545	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	546	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	547	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	548	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	549	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	550	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	551	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	552	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	553	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	554	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	555	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	556	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	557	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	558	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	559	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	560	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
12.9s	561	Collecting nlpaug
12.9s	562	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	563	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	564	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	565	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	566	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	567	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	568	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	569	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	570	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	571	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	572	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	573	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	574	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	575	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	576	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	577	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	578	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	579	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	580	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	581	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	582	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	583	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	584	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	585	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	586	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	587	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	588	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	589	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	590	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	591	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	592	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	593	[?25hInstalling collected packages: nlpaug
16.8s	594	Successfully installed nlpaug-1.1.11
17.7s	595	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	596	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	597	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	598	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	599	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	600	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	601	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	602	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	603	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	604	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	605	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	606	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	607	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	608	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	609	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	610	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	611	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	612	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	613	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	614	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	615	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	616	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	617	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	618	Using device: cuda
6093.7s	619	Stopping early at epoch 9
16050.3s	620	Stopping early at epoch 10
17366.9s	621	Stopping early at epoch 5
39.5s	622	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	623	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	624	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	625	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	626	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	627	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	628	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	629	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	630	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	631	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	632	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	633	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	634	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	635	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	636	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	637	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	638	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
17367.1s	639	[I 2025-01-28 01:57:44,142] Trial 11 finished with value: 0.5747126436781609 and parameters: {'learning_rate': 4.412782360446137e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22861677124968877, 'epochs': 8, 'batch_size': 16, 'step_size': 1, 'gamma': 0.8669394692021379, 'pruning_rate': 0.05915694799122513}. Best is trial 11 with value: 0.5747126436781609.
12.9s	640	Collecting nlpaug
12.9s	641	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	642	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	643	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	644	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	645	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	646	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	647	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	648	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	649	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	650	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	651	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	652	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	653	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	654	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	655	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	656	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	657	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	658	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	659	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	660	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	661	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	662	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	663	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	664	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	665	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	666	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	667	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	668	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	669	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	670	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	671	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	672	[?25hInstalling collected packages: nlpaug
16.8s	673	Successfully installed nlpaug-1.1.11
17.7s	674	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	675	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	676	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	677	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	678	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	679	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	680	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	681	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	682	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	683	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	684	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	685	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	686	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	687	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	688	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	689	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	690	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	691	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	692	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	693	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	694	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	695	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	696	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	697	Using device: cuda
6093.7s	698	Stopping early at epoch 9
16050.3s	699	Stopping early at epoch 10
17366.9s	700	Stopping early at epoch 5
39.5s	701	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	702	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	703	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	704	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	705	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	706	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	707	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	708	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	709	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	710	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	711	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	712	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	713	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	714	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	715	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	716	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	717	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
17367.1s	718	[I 2025-01-28 01:57:44,142] Trial 11 finished with value: 0.5747126436781609 and parameters: {'learning_rate': 4.412782360446137e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22861677124968877, 'epochs': 8, 'batch_size': 16, 'step_size': 1, 'gamma': 0.8669394692021379, 'pruning_rate': 0.05915694799122513}. Best is trial 11 with value: 0.5747126436781609.
12.9s	719	Collecting nlpaug
12.9s	720	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	721	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	722	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	723	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	724	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	725	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	726	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	727	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	728	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	729	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	730	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	731	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	732	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	733	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	734	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	735	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	736	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	737	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	738	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	739	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	740	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	741	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	742	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	743	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	744	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	745	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	746	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	747	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	748	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	749	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	750	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	751	[?25hInstalling collected packages: nlpaug
16.8s	752	Successfully installed nlpaug-1.1.11
17.7s	753	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	754	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	755	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	756	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	757	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	758	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	759	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	760	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	761	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	762	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	763	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	764	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	765	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	766	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	767	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	768	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	769	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	770	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	771	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	772	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	773	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	774	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	775	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	776	Using device: cuda
6093.7s	777	Stopping early at epoch 9
16050.3s	778	Stopping early at epoch 10
17366.9s	779	Stopping early at epoch 5
18905.0s	780	Stopping early at epoch 6
39.5s	781	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	782	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	783	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	784	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	785	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	786	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	787	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	788	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	789	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	790	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	791	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	792	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	793	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	794	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	795	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	796	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	797	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
17367.1s	798	[I 2025-01-28 01:57:44,142] Trial 11 finished with value: 0.5747126436781609 and parameters: {'learning_rate': 4.412782360446137e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22861677124968877, 'epochs': 8, 'batch_size': 16, 'step_size': 1, 'gamma': 0.8669394692021379, 'pruning_rate': 0.05915694799122513}. Best is trial 11 with value: 0.5747126436781609.
18905.2s	799	[I 2025-01-28 02:23:22,229] Trial 12 finished with value: 0.555008210180624 and parameters: {'learning_rate': 5.0710556506436196e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.2546473808356469, 'epochs': 8, 'batch_size': 16, 'step_size': 3, 'gamma': 0.8709633536470471, 'pruning_rate': 0.055279624775367214}. Best is trial 11 with value: 0.5747126436781609.
20581.2s	800	[I 2025-01-28 02:51:18,205] Trial 13 finished with value: 0.5648604269293924 and parameters: {'learning_rate': 4.6372088685295784e-05, 'num_trainable_layers': 3, 'dropout_rate': 0.20924956330538827, 'epochs': 6, 'batch_size': 16, 'step_size': 1, 'gamma': 0.7475783713855387, 'pruning_rate': 0.06956915380322351}. Best is trial 11 with value: 0.5747126436781609.
12.9s	801	Collecting nlpaug
12.9s	802	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	803	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	804	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	805	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	806	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	807	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	808	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	809	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	810	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	811	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	812	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	813	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	814	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	815	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	816	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	817	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	818	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	819	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	820	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	821	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	822	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	823	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	824	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	825	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	826	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	827	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	828	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	829	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	830	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	831	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	832	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	833	[?25hInstalling collected packages: nlpaug
16.8s	834	Successfully installed nlpaug-1.1.11
17.7s	835	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	836	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	837	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	838	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	839	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	840	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	841	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	842	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	843	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	844	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	845	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	846	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	847	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	848	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	849	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	850	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	851	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	852	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	853	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	854	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	855	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	856	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	857	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	858	Using device: cuda
6093.7s	859	Stopping early at epoch 9
16050.3s	860	Stopping early at epoch 10
17366.9s	861	Stopping early at epoch 5
18905.0s	862	Stopping early at epoch 6
39.5s	863	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	864	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	865	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	866	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	867	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	868	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	869	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	870	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	871	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	872	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	873	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	874	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	875	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	876	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	877	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	878	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	879	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
17367.1s	880	[I 2025-01-28 01:57:44,142] Trial 11 finished with value: 0.5747126436781609 and parameters: {'learning_rate': 4.412782360446137e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22861677124968877, 'epochs': 8, 'batch_size': 16, 'step_size': 1, 'gamma': 0.8669394692021379, 'pruning_rate': 0.05915694799122513}. Best is trial 11 with value: 0.5747126436781609.
18905.2s	881	[I 2025-01-28 02:23:22,229] Trial 12 finished with value: 0.555008210180624 and parameters: {'learning_rate': 5.0710556506436196e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.2546473808356469, 'epochs': 8, 'batch_size': 16, 'step_size': 3, 'gamma': 0.8709633536470471, 'pruning_rate': 0.055279624775367214}. Best is trial 11 with value: 0.5747126436781609.
20581.2s	882	[I 2025-01-28 02:51:18,205] Trial 13 finished with value: 0.5648604269293924 and parameters: {'learning_rate': 4.6372088685295784e-05, 'num_trainable_layers': 3, 'dropout_rate': 0.20924956330538827, 'epochs': 6, 'batch_size': 16, 'step_size': 1, 'gamma': 0.7475783713855387, 'pruning_rate': 0.06956915380322351}. Best is trial 11 with value: 0.5747126436781609.
12.9s	883	Collecting nlpaug
12.9s	884	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	885	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	886	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	887	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	888	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	889	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	890	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	891	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	892	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	893	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	894	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	895	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	896	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	897	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	898	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	899	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	900	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	901	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	902	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	903	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	904	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	905	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	906	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	907	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	908	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	909	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	910	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	911	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	912	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	913	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	914	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	915	[?25hInstalling collected packages: nlpaug
16.8s	916	Successfully installed nlpaug-1.1.11
17.7s	917	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	918	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	919	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	920	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	921	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	922	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	923	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	924	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	925	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	926	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	927	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	928	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	929	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	930	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	931	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	932	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	933	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	934	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	935	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	936	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	937	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	938	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	939	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	940	Using device: cuda
6093.7s	941	Stopping early at epoch 9
16050.3s	942	Stopping early at epoch 10
17366.9s	943	Stopping early at epoch 5
18905.0s	944	Stopping early at epoch 6
22340.6s	945	Stopping early at epoch 6
39.5s	946	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	947	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	948	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	949	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	950	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	951	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	952	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	953	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	954	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	955	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	956	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	957	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	958	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	959	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	960	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	961	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	962	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
17367.1s	963	[I 2025-01-28 01:57:44,142] Trial 11 finished with value: 0.5747126436781609 and parameters: {'learning_rate': 4.412782360446137e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22861677124968877, 'epochs': 8, 'batch_size': 16, 'step_size': 1, 'gamma': 0.8669394692021379, 'pruning_rate': 0.05915694799122513}. Best is trial 11 with value: 0.5747126436781609.
18905.2s	964	[I 2025-01-28 02:23:22,229] Trial 12 finished with value: 0.555008210180624 and parameters: {'learning_rate': 5.0710556506436196e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.2546473808356469, 'epochs': 8, 'batch_size': 16, 'step_size': 3, 'gamma': 0.8709633536470471, 'pruning_rate': 0.055279624775367214}. Best is trial 11 with value: 0.5747126436781609.
20581.2s	965	[I 2025-01-28 02:51:18,205] Trial 13 finished with value: 0.5648604269293924 and parameters: {'learning_rate': 4.6372088685295784e-05, 'num_trainable_layers': 3, 'dropout_rate': 0.20924956330538827, 'epochs': 6, 'batch_size': 16, 'step_size': 1, 'gamma': 0.7475783713855387, 'pruning_rate': 0.06956915380322351}. Best is trial 11 with value: 0.5747126436781609.
22340.8s	966	[I 2025-01-28 03:20:37,877] Trial 14 finished with value: 0.5623973727422004 and parameters: {'learning_rate': 4.563901483167541e-05, 'num_trainable_layers': 3, 'dropout_rate': 0.29273024197221564, 'epochs': 8, 'batch_size': 16, 'step_size': 4, 'gamma': 0.5207269386645943, 'pruning_rate': 0.042589414119157336}. Best is trial 11 with value: 0.5747126436781609.
12.9s	967	Collecting nlpaug
12.9s	968	  Downloading nlpaug-1.1.11-py3-none-any.whl.metadata (14 kB)
12.9s	969	Requirement already satisfied: numpy>=1.16.2 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (1.26.4)
12.9s	970	Requirement already satisfied: pandas>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.2.2)
12.9s	971	Requirement already satisfied: requests>=2.22.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (2.32.3)
12.9s	972	Requirement already satisfied: gdown>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from nlpaug) (5.2.0)
12.9s	973	Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.12.3)
12.9s	974	Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (3.16.1)
12.9s	975	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from gdown>=4.0.0->nlpaug) (4.67.1)
12.9s	976	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.3.8)
12.9s	977	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (1.2.4)
12.9s	978	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (0.1.1)
12.9s	979	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2025.0.1)
12.9s	980	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2022.0.0)
12.9s	981	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy>=1.16.2->nlpaug) (2.4.1)
13.0s	982	Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2.8.2)
13.0s	983	Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	984	Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.2.0->nlpaug) (2024.2)
13.0s	985	Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.4.0)
13.0s	986	Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (3.10)
13.0s	987	Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2.2.3)
13.0s	988	Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.22.0->nlpaug) (2024.12.14)
13.0s	989	Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=1.2.0->nlpaug) (1.17.0)
13.0s	990	Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->gdown>=4.0.0->nlpaug) (2.6)
13.0s	991	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	992	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy>=1.16.2->nlpaug) (2022.0.0)
13.0s	993	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy>=1.16.2->nlpaug) (1.2.0)
13.0s	994	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy>=1.16.2->nlpaug) (2024.2.0)
13.0s	995	Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->gdown>=4.0.0->nlpaug) (1.7.1)
13.0s	996	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy>=1.16.2->nlpaug) (2024.2.0)
13.1s	997	Downloading nlpaug-1.1.11-py3-none-any.whl (410 kB)
13.1s	998	[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/410.5 kB[0m [31m?[0m eta [36m-:--:--[0m
[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m[90m━━━━━[0m [32m358.4/410.5 kB[0m [31m10.5 MB/s[0m eta [36m0:00:01[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m410.5/410.5 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
16.5s	999	[?25hInstalling collected packages: nlpaug
16.8s	1000	Successfully installed nlpaug-1.1.11
17.7s	1001	Requirement already satisfied: optuna in /usr/local/lib/python3.10/dist-packages (4.1.0)
17.7s	1002	Requirement already satisfied: alembic>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (1.14.0)
17.7s	1003	Requirement already satisfied: colorlog in /usr/local/lib/python3.10/dist-packages (from optuna) (6.9.0)
17.7s	1004	Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from optuna) (1.26.4)
17.7s	1005	Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from optuna) (24.2)
17.7s	1006	Requirement already satisfied: sqlalchemy>=1.4.2 in /usr/local/lib/python3.10/dist-packages (from optuna) (2.0.36)
17.7s	1007	Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from optuna) (4.67.1)
17.7s	1008	Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from optuna) (6.0.2)
17.7s	1009	Requirement already satisfied: Mako in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (1.3.8)
17.7s	1010	Requirement already satisfied: typing-extensions>=4 in /usr/local/lib/python3.10/dist-packages (from alembic>=1.5.0->optuna) (4.12.2)
17.8s	1011	Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from sqlalchemy>=1.4.2->optuna) (3.1.1)
17.8s	1012	Requirement already satisfied: mkl_fft in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.3.8)
17.8s	1013	Requirement already satisfied: mkl_random in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (1.2.4)
17.8s	1014	Requirement already satisfied: mkl_umath in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (0.1.1)
17.8s	1015	Requirement already satisfied: mkl in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2025.0.1)
17.8s	1016	Requirement already satisfied: tbb4py in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2022.0.0)
17.8s	1017	Requirement already satisfied: mkl-service in /usr/local/lib/python3.10/dist-packages (from numpy->optuna) (2.4.1)
17.8s	1018	Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from Mako->alembic>=1.5.0->optuna) (3.0.2)
17.8s	1019	Requirement already satisfied: intel-openmp>=2024 in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2024.2.0)
17.8s	1020	Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.10/dist-packages (from mkl->numpy->optuna) (2022.0.0)
17.8s	1021	Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.10/dist-packages (from tbb==2022.*->mkl->numpy->optuna) (1.2.0)
17.8s	1022	Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.10/dist-packages (from mkl_umath->numpy->optuna) (2024.2.0)
17.8s	1023	Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.10/dist-packages (from intel-openmp>=2024->mkl->numpy->optuna) (2024.2.0)
83.1s	1024	Using device: cuda
6093.7s	1025	Stopping early at epoch 9
16050.3s	1026	Stopping early at epoch 10
17366.9s	1027	Stopping early at epoch 5
18905.0s	1028	Stopping early at epoch 6
22340.6s	1029	Stopping early at epoch 6
39.5s	1030	2025-01-27 21:08:56.523904: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
39.9s	1031	2025-01-27 21:08:56.929966: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
40.0s	1032	2025-01-27 21:08:57.046411: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
112.1s	1033	[I 2025-01-27 21:10:09,128] A new study created in memory with name: no-name-29ef3950-2a0d-46b4-baa2-d13b362395c2
114.0s	1034	<ipython-input-10-2d9dfced9ac1>:11: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
114.0s	1035	  item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
1451.0s	1036	[I 2025-01-27 21:32:28,013] Trial 0 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 8.300432875328772e-05, 'num_trainable_layers': 2, 'dropout_rate': 0.3847406475130443, 'epochs': 5, 'batch_size': 32, 'step_size': 9, 'gamma': 0.5951936405857416, 'pruning_rate': 0.041233631545798136}. Best is trial 0 with value: 0.5443349753694581.
2076.9s	1037	[I 2025-01-27 21:42:53,945] Trial 1 finished with value: 0.5311986863711001 and parameters: {'learning_rate': 9.449184169316452e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.15905196093024393, 'epochs': 2, 'batch_size': 32, 'step_size': 9, 'gamma': 0.16999909235452987, 'pruning_rate': 0.08306303717178752}. Best is trial 0 with value: 0.5443349753694581.
3159.7s	1038	[I 2025-01-27 22:00:56,769] Trial 2 finished with value: 0.5090311986863711 and parameters: {'learning_rate': 0.0005379695375957465, 'num_trainable_layers': 2, 'dropout_rate': 0.34335698709065776, 'epochs': 4, 'batch_size': 64, 'step_size': 9, 'gamma': 0.12489069375484957, 'pruning_rate': 0.09649309801422111}. Best is trial 0 with value: 0.5443349753694581.
6093.9s	1039	[I 2025-01-27 22:49:50,973] Trial 3 finished with value: 0.5443349753694581 and parameters: {'learning_rate': 1.3224632569564986e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4297597513790551, 'epochs': 9, 'batch_size': 16, 'step_size': 6, 'gamma': 0.14230292148368884, 'pruning_rate': 0.023981488127990426}. Best is trial 0 with value: 0.5443349753694581.
6906.1s	1040	[I 2025-01-27 23:03:23,122] Trial 4 finished with value: 0.5533661740558292 and parameters: {'learning_rate': 0.00015107245591067491, 'num_trainable_layers': 2, 'dropout_rate': 0.49267405751084237, 'epochs': 3, 'batch_size': 64, 'step_size': 7, 'gamma': 0.19092196015418106, 'pruning_rate': 0.022438507494380082}. Best is trial 4 with value: 0.5533661740558292.
8017.9s	1041	[I 2025-01-27 23:21:54,912] Trial 5 finished with value: 0.5706075533661741 and parameters: {'learning_rate': 0.00010950086269075686, 'num_trainable_layers': 2, 'dropout_rate': 0.1944664466713519, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.504876871310878, 'pruning_rate': 0.05160234955940831}. Best is trial 5 with value: 0.5706075533661741.
9965.4s	1042	[I 2025-01-27 23:54:22,407] Trial 6 finished with value: 0.5545529122231337 and parameters: {'learning_rate': 2.6161416348231633e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.4133579503968431, 'epochs': 6, 'batch_size': 32, 'step_size': 9, 'gamma': 0.6378121697091345, 'pruning_rate': 0.05443003303694141}. Best is trial 5 with value: 0.5706075533661741.
10622.8s	1043	[I 2025-01-28 00:05:19,842] Trial 7 finished with value: 0.32922824302134646 and parameters: {'learning_rate': 1.3142236020960931e-05, 'num_trainable_layers': 6, 'dropout_rate': 0.48194997736207845, 'epochs': 2, 'batch_size': 64, 'step_size': 3, 'gamma': 0.3424915421431794, 'pruning_rate': 0.03655243267792772}. Best is trial 5 with value: 0.5706075533661741.
11248.6s	1044	[I 2025-01-28 00:15:45,621] Trial 8 finished with value: 0.31829368334700575 and parameters: {'learning_rate': 0.00035281177564274314, 'num_trainable_layers': 5, 'dropout_rate': 0.42012582229319084, 'epochs': 2, 'batch_size': 64, 'step_size': 5, 'gamma': 0.7031141087320367, 'pruning_rate': 0.07506936055122124}. Best is trial 5 with value: 0.5706075533661741.
13063.4s	1045	[I 2025-01-28 00:46:00,471] Trial 9 finished with value: 0.5668580803937654 and parameters: {'learning_rate': 2.1598436452319275e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22983060124773347, 'epochs': 7, 'batch_size': 32, 'step_size': 2, 'gamma': 0.8674344229845424, 'pruning_rate': 0.09424523130732962}. Best is trial 5 with value: 0.5706075533661741.
16050.6s	1046	[I 2025-01-28 01:35:47,620] Trial 10 finished with value: 0.29802955665024633 and parameters: {'learning_rate': 0.00021215522071577303, 'num_trainable_layers': 4, 'dropout_rate': 0.10295160865478536, 'epochs': 10, 'batch_size': 16, 'step_size': 1, 'gamma': 0.42138611070554194, 'pruning_rate': 0.06291413799922993}. Best is trial 5 with value: 0.5706075533661741.
17367.1s	1047	[I 2025-01-28 01:57:44,142] Trial 11 finished with value: 0.5747126436781609 and parameters: {'learning_rate': 4.412782360446137e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.22861677124968877, 'epochs': 8, 'batch_size': 16, 'step_size': 1, 'gamma': 0.8669394692021379, 'pruning_rate': 0.05915694799122513}. Best is trial 11 with value: 0.5747126436781609.
18905.2s	1048	[I 2025-01-28 02:23:22,229] Trial 12 finished with value: 0.555008210180624 and parameters: {'learning_rate': 5.0710556506436196e-05, 'num_trainable_layers': 1, 'dropout_rate': 0.2546473808356469, 'epochs': 8, 'batch_size': 16, 'step_size': 3, 'gamma': 0.8709633536470471, 'pruning_rate': 0.055279624775367214}. Best is trial 11 with value: 0.5747126436781609.
20581.2s	1049	[I 2025-01-28 02:51:18,205] Trial 13 finished with value: 0.5648604269293924 and parameters: {'learning_rate': 4.6372088685295784e-05, 'num_trainable_layers': 3, 'dropout_rate': 0.20924956330538827, 'epochs': 6, 'batch_size': 16, 'step_size': 1, 'gamma': 0.7475783713855387, 'pruning_rate': 0.06956915380322351}. Best is trial 11 with value: 0.5747126436781609.
22340.8s	1050	[I 2025-01-28 03:20:37,877] Trial 14 finished with value: 0.5623973727422004 and parameters: {'learning_rate': 4.563901483167541e-05, 'num_trainable_layers': 3, 'dropout_rate': 0.29273024197221564, 'epochs': 8, 'batch_size': 16, 'step_size': 4, 'gamma': 0.5207269386645943, 'pruning_rate': 0.042589414119157336}. Best is trial 11 with value: 0.5747126436781609.
23344.9s	1051	[I 2025-01-28 03:37:21,994] Trial 15 finished with value: 0.5558292282430214 and parameters: {'learning_rate': 0.00022741975752929195, 'num_trainable_layers': 1, 'dropout_rate': 0.1895626628958686, 'epochs': 4, 'batch_size': 16, 'step_size': 1, 'gamma': 0.31396273274373876, 'pruning_rate': 0.054432434473777665}. Best is trial 11 with value: 0.5747126436781609.
24908.5s	1052	Stopping early at epoch 6
24908.7s	1053	[I 2025-01-28 04:03:25,795] Trial 16 finished with value: 0.2947454844006568 and parameters: {'learning_rate': 0.0007451756222197525, 'num_trainable_layers': 2, 'dropout_rate': 0.1356457817137555, 'epochs': 6, 'batch_size': 16, 'step_size': 3, 'gamma': 0.7746224841774176, 'pruning_rate': 0.033751176401978944}. Best is trial 11 with value: 0.5747126436781609.
