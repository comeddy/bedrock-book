# 'Amazon Bedrock 생성형 AI 앱 개발 입문' 핸즈온용 샘플 코드

제목 책의 핸즈온을 쉽게 할 수 있도록 샘플 코드 부분을 파일로 저장한 리포지토리입니다.

- 책을 구매하신 분들도 복사 및 붙여넣기가 가능합니다.
- 향후 환경 변화로 인해 코드에 문제가 발생할 경우, 수시로 수정해 나갈 예정입니다.

## 📗 GitHub 저장소 설명

### 책에 대하여

아직 가지고 있지 않으신 분은 꼭 구입해 보세요!

[Amazon Bedrock 생성형 AI 앱 개발 입문](https://www.sbcr.jp/product/4815626440/)

![](images/flyer.png)

### 이 리포지토리 구성

- `chapter⚫️` 디렉토리: 각 장과 수동으로 입력하기 어려운 설정에 대한 실습 코드가 들어 있습니다.
  - 필요한 Python 라이브러리를 나열한 `requirements.txt`도 참고로 저장됩니다.
  - 서적 간행 후 기능 업데이트에 대응하는 방법 등을 `README.md`로 보충하고 있습니다.
  
### 오류 등을 발견하면

책 저장소 [Issues](https://github.com/minorun365/bedrock-book/issues)에 기표해 주세요. 최선을 다해 대응하겠습니다.

### 오탈자 등 안내

[SBクリエイティブ公式サイト](https://www.sbcr.jp/product/4815626440/) 에 오류 정보를 수시로 게재합니다.


## ✨ 책 출간 후 업데이트 보충

### ■ Cloud9의 신규 이용 불가 (대상: 부록 4 및 핸즈온 전반)

실습용 개발 환경으로 안내하고 있는 AWS Cloud9의 신규 이용이 2024/7/29부터 일부 제한되었음을 확인하였습니다.
부록 4를 대체할 수 있는 절차를 아래 블로그 글에 공개했습니다. 각 장에 대한 재검증을 진행하고 있으며, 내용은 수시로 업데이트하고 있습니다.

[AWS Cloud9이 갑자기 신규 이용 불가? 대체 방안 'SageMaker Studio 코드 에디터' 이용 방법](https://qiita.com/minorun365/items/f5289163795d5d7b21e2)

### ■ 신모델 추가(대상: 2장 외)

#### 【2024/6/20】 Anthropic의 새로운 모델 'Claude 3.5 Sonnet' 출시!

Anthropic의 새로운 모델로 Claude 3 Sonnet의 후속 모델이다. 성능, 비용 모두 Claude 3 Opus를 능가하는 것으로 알려져 있다.

- https://qiita.com/minorun365/items/cd46235d5e446b1f41c5

이 책의 핸즈온 활용 방법

- 책 P.80을 참고하여 `Claude 3.5 Sonnet`을 버지니아 북부 지역 Bedrock에서 활성화하기
  - '사용 불가' 상태가 되어 활성화되지 않을 수 있습니다. 이 경우 시간을 두고 다시 시도하거나 AWS 지원팀에 문의해 보시기 바랍니다.
- 각 장의 샘플 코드에서 Claude 3 Sonnet의 모델 ID를 지정한 부분을 Claude 3.5 Sonnet의 모델 ID(`anthropic.claude-3-5-sonnet-20240620-v1:0`)로 대체한다.

주의 사항

- Bedrock에서는 GUI나 API를 통한 단독 모델 호출은 지원하지만, 응용 기능(지식 베이스나 에이전트)은 미지원입니다(2024/6/20 기준).
- Knowkedge bases for Amazon Bedrock에서는 `Retrieve` API를 이용하면 Claude 3.5 Sonnet을 바로 활용할 수 있습니다(책 P.216 참조).

#### 【2024/6/26】 AI21 Labs의 새로운 모델 'Jumba-Instruct'가 출시되었습니다.

기존 'Jurassic-2' 시리즈를 뛰어넘는 고성능 모델로, 256K 토큰의 대용량 컨텍스트 창을 지원한다. 언어는 영어만 지원.

- [AI21 Labs Jamba-Instruct model is now available in Amazon Bedrock | AWS Machine Learning Blog](https://aws.amazon.com/jp/blogs/machine-learning/ai21-labs-jamba-instruct-model-is-now-available-in-amazon-bedrock/)

#### 【2024/7/24】 Meta社의 새로운 모델 'Llama 3.1' 시리즈 출시

기존 모델인 'Llama 3' 시리즈의 후속 모델이다.

- [Meta, Amazon Bedrock에서 Llama 3.1 405B, 70B 및 8B 모델 발표| Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/announcing-llama-3-1-405b-70b-and-8b-models-from-meta-in-amazon-bedrock/)

#### 【2024/7/25】 미스트랄의 새로운 모델 '미스트랄 라지 2'가 출시되었습니다.

- [Mistral Large 2 is now available in Amazon Bedrock | AWS Machine Learning Blog](https://aws.amazon.com/jp/blogs/machine-learning/mistral-large-2-is-now-available-in-amazon-bedrock/)

#### 【2024/8/6】 Claude 3 시리즈가 AWS 도쿄 리전에 대응합니다.

- [AWS 도쿄 리전의 Bedrock에서 Claude 3.5 Sonnet을 사용할 수 있게 되었습니다.🎉](https://qiita.com/minorun365/items/e2202774ea357f311243)

#### 【2024/8/6】 아마존의 새로운 모델 'Titan Image Generator v2'가 출시되었습니다.

- [Amazon Titan Image Generator G1 V2と戯れる（Gradioがおすすめ）](https://qiita.com/moritalous/items/29c4d4736d794b75f346)
- [Amazon Bedrock で Amazon Titan Image Generator v2 が利用可能に](https://aws.amazon.com/jp/blogs/news/amazon-titan-image-generator-v2-is-now-available-in-amazon-bedrock/)

#### 【2024/9/4】 Stability AI社의 신모델 「Stable Image Ultra」「Stable Diffusion 3 Large (SD3 Large)」「Stable Image Core」출시

- [Bedrock에 AI의 새로운 이미지 생성 모델 3종이 추가되었습니다.！](https://qiita.com/hedgehog051/items/446db1c07ac45eea1c9c)

### ■ Bedrock 응용 기능 업데이트 (대상 : 4~6장 외)

#### 【2024/7/11】 생성 AI 관련 대형 업데이트 다수 (Bedrock, Amazon Q, 기타 신규 서비스 등)

해설 슬라이드를 공개합니다. 이 책을 읽으신 분들은 업데이트를 더 쉽게 이해하실 수 있을 것입니다!

- [宇宙最速で7/11未明のAmazon Bedrock大型アプデを解説 🚀 - Speaker Deck](https://speakerdeck.com/minorun365/11wei-ming-noamazon-bedrockda-xing-apudewojie-shuo)

#### 【2024/8/21】 Bedrock의 일괄 추론 기능 일반 제공 시작

'6.4.1 일괄 추론'에서 설명한 기능이 일반에 제공되기 시작했습니다. 전용 SDK가 필요 없이 사용할 수 있습니다.

- [Amazon Bedrock 는 일괄 추론용 엄선된 FM을 온디맨드 추론 가격의 50%에 제공하고 있습니다.](https://aws.amazon.com/jp/about-aws/whats-new/2024/08/amazon-bedrock-fms-batch-inference-50-price/)

#### 【2024/8/27】 지역 간 추론 지원

여러 지역을 사용한 동적 라우팅을 지원했습니다. 예를 들어, 'US Anthropic Claude 3.5 Sonnet'을 지정하면 버지니아 북부와 오리건 리전을 사용하여 추론할 수 있다. 지정 방법은 모델 ID로 inference profile(전용 모델 ID)을 지정합니다. (예: us.anthropic.claude-3-5-sonnet-20240620-v1:0)

- [Amazon Bedrock 에서 리전 간 추론 지원 시작](https://aws.amazon.com/jp/about-aws/whats-new/2024/08/amazon-bedrock-cross-region-inference/)

### ■ Amazon Q 업데이트 (대상: 9장)

#### 2024년 내] Amazon Q Business가 일본어 및 AWS 도쿄 리전에 대응 예정

참고 기사(Cloud Watch)

- [AWS, Claude 3 및 Amazon Q for Business 일본어판 도쿄 리전 제공 시기 등 공개 - Cloud Watch](https://cloud.watch.impress.co.jp/docs/event/1601745.html)

### LangChain 버전 0.3.0 출시

LangChain의 새로운 버전 '0.3.0'이 출시되었습니다. (책 집필 당시에는 0.2.0이었습니다.) 3장, 4장, 5장에서 LangChain을 사용하고 있는데, 라이브러리 버전업만으로 동작하는 것을 확인했습니다. 동작을 확인한 디렉토리에 'requirements_langchain-0.3.0.txt'를 저장해 두었으니, LangChain 0.3.0에서 실행할 때는 아래 명령어로 설치하시기 바랍니다.

```
pip install -r requirements_langchain-0.3.0.txt
```


## 💻 독자 여러분들의 서평 블로그 소개

좋은 결과물 많이 만들어 주셔서 감사합니다! 🙇‍♂️

- おむろんさん [「Amazon Bedrock生成AIアプリ開発入門」本の感想を宇宙最速で述べる #Bedrock開発入門 - omuronの備忘録](https://omuron.hateblo.jp/entry/2024/06/18/151000)
- cyberBOSEさん [「Amazon Bedrock 生成AIアプリ開発入門」レビュー #Bedrock開発入門 #Python - Qiita](https://qiita.com/cyberBOSE/items/c2b0a2885b79f4d10f5d)
- s.hirutaさん [Bedrock開発入門書籍レビュー | クラウドインフラ構築記](https://www.totalsolution.biz/bedrock%e9%96%8b%e7%99%ba%e5%85%a5%e9%96%80%e6%9b%b8%e7%b1%8d%e3%83%ac%e3%83%93%e3%83%a5%e3%83%bc/)
- hmatsu47さん [Amazon Bedrock 生成 AI アプリ開発入門［AWS 深掘りガイド］の紹介 - 構築中。](https://hmatsu47.hatenablog.com/entry/2024/06/19/210808)
- Renya K.さん [「Amazon Bedrock」で始める生成AIアプリ開発入門バイブルの登場！！ #AWS - Qiita](https://qiita.com/ren8k/items/6134d2457211e5a285c4)
- hayao_kさん [Amazon Bedrock 生成AIアプリ開発入門 レビュー #Bedrock開発入門 #AWS - Qiita](https://qiita.com/hayao_k/items/fcd4d9921510ead0fee3)
- 星野ぽぽぽさん [【書評】Amazon Bedrock 生成 AI アプリ開発入門｜星野ぽぽぽ(noteのすがた)](https://note.com/hoshino_popopo_/n/nbef8bb5cc07f)
- kazzpapa3さん [Amazon Bedrock 生成AIアプリ開発入門 の書評 という名の雑記 - ほぼ自分のための備忘録ブログ](https://blog.kazzpapa3.com/blog/2024/06/26/amazon-bedrock-ai/)
- 石原直樹さん [「Amazon Bedrock 生成AIアプリ開発入門」 レビュー #Bedrock開発入門 #AWS - Qiita](https://qiita.com/Naoki_Ishihara/items/589e8ac423ed2a5ffcee)
- kzk_maedaさん [Bedrock開発入門を読みました｜kzk_maeda](https://note.com/kzk_maeda/n/nffa11ccb9389?sub_rt=share_pb)
- 山本紘暉さん [【書評】Amazon Bedrock 生成AIアプリ開発入門 [AWS深掘りガイド] | DevelopersIO](https://dev.classmethod.jp/articles/book-review-amazon-bedrock-genai-app-dev-intro/)
- つくぼしさん [AWSにおける生成AIアプリ開発を学ぶには最適の入門書「Amazon Bedrock 生成AIアプリ開発入門」 | DevelopersIO](https://dev.classmethod.jp/articles/review-bedrock-genai-app-dev-intro/)
- 平野文雄さん [「Amazon Bedrock 生成AIアプリ開発入門」のススメ | DevelopersIO](https://dev.classmethod.jp/articles/recommend-bedrock-genai-app-dev-intro/)
- Akihiro Uenoさん [『Amazon Bedrock 生成AIアプリ開発入門』の感想をば](https://zenn.dev/ueniki/articles/50c73a94b186ce)
- yuki_inkさん [『Amazon Bedrock 生成AIアプリ開発入門』 から始めるAIエージェント #AWS - Qiita](https://qiita.com/yuki_ink/items/097bbe9893359e12996f?utm_campaign=post_article&utm_medium=twitter&utm_source=twitter_share)
- しまさん [【感想】『Amazon Bedrock 生成AIアプリ開発入門』を読みました](https://zenn.dev/os1ma/articles/27bf3bd821065d)
- mongolyyさん [「Amazon Bedrock 生成AIアプリ開発入門 」を読んだ - mongolyyのブログ](https://mongolyy.hatenablog.com/entry/2024/08/15/131247)
- issyさん [書籍「Amazon Bedrock 生成AIアプリ開発入門-第４章-」 × AWS Summit Japan 2024](https://zenn.dev/issy/articles/bedrock-book-aws-summit-2024)
- Shinodaさん [書評「Amazon Bedrock 生成AIアプリ開発入門」｜Shinoda](https://note.com/yukkie1114/n/nb97f45b13a2f)
- MK_Techさん [『感想』Amazon Bedrock生成AIアプリ開発入門 #AWS - Qiita](https://qiita.com/MK_Tech/items/a443fb394abbeb2bae60)
- Masaru Oguraさん [Amazon Bedrock 生成AIアプリ開発入門の感想文｜Masaru Ogura](https://note.com/masaruogura/n/n2cb9a66aa4cf?sub_rt=share_pb)
