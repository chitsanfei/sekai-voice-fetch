<div align="center">
    <hr>
    <img src="https://raw.githubusercontent.com/MashiroSA/sekai-voice-fetch/master/assets/img/stamp.png" height="200" alt="sekai-voice-fetch"> 
    <h1>sekai-voice-fetch</h1>
    <b>一个用于爬取sekai.best网站中角色的对话语音的爬虫？</b>
</div>

---

[![Github Issue](https://img.shields.io/github/issues/MashiroSA/sekai-voice-fetch)](https://github.com/MashiroSA/sekai-voice-fetch/issues)
[![Github Forks](https://img.shields.io/github/forks/MashiroSA/sekai-voice-fetch)](https://github.com/MashiroSA/sekai-voice-fetch/fork)
[![Github Stars](https://img.shields.io/github/stars/MashiroSA/sekai-voice-fetch)](https://github.com/MashiroSA/sekai-voice-fetch)
[![GitHub License](https://img.shields.io/github/license/MashiroSA/sekai-voice-fetch)](https://github.com/MashiroSA/sekai-voice-fetch/blob/master/LICENSE)

---

![Alt](https://repobeats.axiom.co/api/embed/27ead3353d126b5d5008a85afedf019e30ec3531.svg "Repobeats analytics image")

---

## 介绍
最近在做电子鳳えむ嘛，额兄弟们大家都知道我喜欢的角色就是emu了，我有`emu电子化训练的程序，emu的彩卡，emu的二次元角色图，emu的附庸ChatGpt，emu的爱`。可以说所有有关emu的东西我都有了，可是大家都知道emu喜欢唱歌，我还没有给她赛博唱歌的条件。那么我还缺什么？哦！我还缺emu的语音数据集。

于是想着手动下载数据集的，后来确实感觉麻烦，所以不小心写了个这个，感觉问题还是很多，但是勉强能用。

数据集的获取主要来源自`sekai.best`中的角色对话和活动对话资源。设计思路是：`循环模拟访问直至js加载完成-获取网页元素-遍历并找寻到以mp3结尾的链接-过滤以获取指定角色id的链接-下载`。

请不要使用过多给`sekai.best`造成困扰哦！

## 文件结构

```
├── config
│   └── setting_fetch.ini #配置文件，在运行前你必须先配置这个文件
├── logger #logger包，主要管理日志功能
│   ├── LogManager.py
│   ├── __init__.py
│   └── logs #日志
├── main.py #程序入口点
├── requirements.txt #依赖
├── sekai #sekai包，主要管理模拟访问和下载
│   ├── Voice.py
│   ├── __init__.py
│   └── resource #下载到的文件都存放在这个文件夹里
│
├── tests
└── venv
```


## 使用方法

### 配置
- 打开配置文件`config/setting_fetch.ini`
```file
[DEFAULT]
url = https://sekai.best/storyreader/eventStory/15/6
interval = 30
character = 14
```
- 填写或修改你所要爬取的角色语音的story链接到url。
- 修改角色id项目character，相应的角色id请自行到sekai.best的故事板的下载语音的文件名查看，如`voice_ev_wonder_03_01_02_14.mp3`是emu的语音，角色的id是14。
- 如有需要，可以继续修改下载间隔interval(默认30秒)，请勿调整过小，极容易触发`502`。

### 运行
> Python > 3.8, Test by Python 3.10
> 
> 建议启用虚拟环境venv
```bash
  pip install -r requirements.txt
```
```bash
  python3 ./main.py
```

## 许可证

`sekai-voice-fetch` 采用 `MIT` 许可证进行开源

```text
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

请注意！使用本程序你将默认同意，所有资源的版权方归`Project Sekai`和`SEGA`以及资源托管站（及其他们的许可要求），本程序和`SEGA`和资源站`sekai.best`团体没有关系，您将保证不对二者产生任何不利影响。本程序仅供进行技术学习和交流，使用本程序所带来的一切法律后果由用户自行承担。

## 感谢
感谢sekai.best资源站为大家提供关于PJSK的资源服务。
Copilot真好用！还有ChatGPT！
