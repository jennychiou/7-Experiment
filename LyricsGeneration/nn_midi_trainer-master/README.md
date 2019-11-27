# nn_midi_trainer

​	Midi trainer & generator with Neural Network.

## Build Environment

- Python 2.7 ( Anaconda Package )

## Article Link

- [google docs](https://docs.google.com/document/d/11RYTlprImsKv4xz-PPzZHm5vkQJ9mWkFil5AaqyKkAE/edit?usp=shari)

##목표

- 1차: 현재 C++ 버전을 Python Tensorflow  버전으로 변환. (현재는 1CPU에서 밤새 훈련이 필요했기 때문에 GPU 사용시 속도 향상을 기대)
- 2차: 훈련 품질 높이기 (완전 암기- 현재는 이전 음에서 다음 음 출력, 출력할 음 결정 방법 - 현재는 주사위)
- 3차: 더 많은 곡들 테스트

##Meeting

###0

- 미디 데이터를 훈련 데이터로 바꿔주는 모듈을 파이썬 버전으로 만들기 (파이썬 모듈이 별도로 들었음)  
- 피아노 연주 모듈 파이썬으로 개발 (이것도 파이썬 모듈이 있을 경우 더 쉬움)
- NN을 Python TF로 구현 (어렵지 않음)
- 데이터 구조 개선 및 추가 테스트 (여기서부터는 미지의 영역)
- 코드 정리 및 깃헙 공개 (readme파일에 참여자 이름과 이메일 주소 넣는 것 잊지 마세요)
- 기고문 문서 작성 

###1 20161117
Piano player (pygame wav play, https://github.com/Calysto/chuck) 조동헌 -> play one wav, multiple channel, sync-async [complete - need enhancement with synthysizer]

Midi reading (MIDO) 정종현, 유선우, CDH [complete]

###2 20161121

Data structure for training - CDH [complete]
Tensorflow NN (FCNN) - CDH [ complete but need enhancement ]

###3

Model improvement, harmony - CDH [complete], Spontaneous play

###4

Test
Initial 24 lengths from midi => generating recursive

###5

Review

Outline

#### Introduction (Previous Work)

summarize each reference in 2-3 sentences.

#### Learning Base Music Generator

[Deep Jazz](https://github.com/jisungk/deepjazz/blob/master/generator.py)

- Jazz음악을 작곡해주는 프로그램. 두개의 LSTM layer를 통해 학습함. Deep Learning 라이브러리인 Keras와 Theano를 이용하여 만들어짐. bpm을 사전에 설정.

[Magenta from Google](https://magenta.tensorflow.org/welcome-to-magenta)

- Magenta는 Google Brain Team가 제공하는 머신러닝을 이용한 art & music 생성기. 현재는 music generator만 제공하고 있으며 recurrent neural network 모델[Basic+LSTM, Lookback, Attention]을 통해 학습되고 있음. 초기 Initial 음을 model에 주면 그에 기반하여 음악을 생성. [ppt](https://drive.google.com/drive/folders/0B8z5oUpB2DysbFNEOWxfVDh5VW8)

[music generate with rnn](http://davinnovation.github.io/old_/midi_generate_rnn.html) 

- RNN모델을로 개발된 music 생성기. n-gram 언어 모델을 기반으로 음악을 학습함. 초기 Initial 음을 주지 않고 처음부터 음악을 생성.

#### Rule Base Music Generator

[WolframTones](http://tones.wolfram.com/)

- 공대의 친구 WolframAlpha 제작사에서 만든 음악 생성기로 각 장르에 맞는 규칙을 통해 음악을 생성

[Jukedeck](https://www.jukedeck.com/)
- 미국 스타트업으로 장르에 기반한 음악을 생성. WolframTone보다 간편한 옵션 설정으로 생성됨. 

#### Piano player

test 완료. package 개발 중 -> explanation

#### Midi reading

미디파일을 읽어들이기 위해 mido 모듈을 사용했다.
readmidi() : 파일 전체를 읽으면서 note와 시작시간을 알아내어 eventlist에 저장한다. eventlist 에서 간격을 나눈 시간내에 note가 있을때 playlist에 추가한다. 그리고 playlist를 반환한다.
makeMidi_nn(playlist,24) : hisotory를 24로 설정하고 한 batch당 88key*24history  2차원 배열을 생성한다. 

#### Data structure for training

exp

#### Tensorflow NN (FCNN)

activation, multi-hidden layer, ...

#### Results and discussion

- moon light, epoch vs accuracy
- additional...

#### Conclusion

- Future work: training data format and note duration
- Github link

## Related Paper
- [music generation with wave learning paper](http://www.gitxiv.com/posts/WEoQCj8hxHz6vPxe6/gruv-algorithmic-music-generation-using-recurrent-neural)
- [KDD 2016 rap lyrics generator paper](http://www.kdd.org/kdd2016/papers/files/adf0399-malmiA.pdf)

## Contributors

정종현, [조동헌](https://github.com/davinnovation), 유선우, 김준기, 홍정모
