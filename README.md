# 🎯 EmoRadar

Real-time learning emotion detection system powered by IBM Watsonx Vision AI, featuring advanced facial expression analysis, educational psychology insights, and intelligent intervention recommendations.

![EmoRadar](https://img.shields.io/badge/AI-Powered-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![IBM Watsonx](https://img.shields.io/badge/IBM-Watsonx-052FAD)

## ✨ Features

- **🎥 Real-Time Analysis**: Computer vision-powered emotion detection using LLaMA 90B Vision Model
- **🧠 Educational Psychology**: Evidence-based intervention recommendations for optimal learning
- **📊 Multi-Dimensional Visualization**: Interactive radar charts and emotion timeline tracking
- **🎯 Learning Optimization**: Personalized insights for engagement, confidence, and focus enhancement
- **⚡ Intelligent Interventions**: Automated detection of when students need support or encouragement
- **🎨 Modern UI**: Professional interface with animated elements and responsive design

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- IBM Watsonx account with Vision AI access
- Webcam or camera for real-time emotion capture

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/JesseChan5171/EmoRadar.git
cd EmoRadar
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Environment Setup**
```bash
cp .env.example .env
# Edit .env with your IBM Watsonx credentials
```

4. **Run the application**
```bash
streamlit run app.py
```

## ⚙️ Configuration

### Required Environment Variables

Create a `.env` file with your IBM Watsonx credentials:

```bash
# IBM Watsonx AI API
WATSONX_API_KEY=your_watsonx_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
```

### Getting IBM Watsonx Credentials

1. Sign up for [IBM Cloud](https://cloud.ibm.com/)
2. Create a Watsonx project at [IBM Watsonx](https://dataplatform.cloud.ibm.com/wx)
3. Get your API key from IBM Cloud console → Manage → Access (IAM) → API keys
4. Copy your project ID from Watsonx project settings

## 📁 Project Structure

```
EmoRadar/
├── app.py                    # Main Streamlit application
├── emotion_detector.py       # Core IBM Watsonx Vision AI integration
├── emotion_visualizer.py     # Advanced visualization engine
├── intervention_engine.py    # Intelligent intervention system
├── requirements.txt          # Python dependencies
├── .env.example             # Environment template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🔧 Usage

### Basic Emotion Analysis
1. Launch the application with `streamlit run app.py`
2. Position yourself clearly in the camera frame
3. Click "Capture image for emotion analysis"
4. View real-time emotion analysis and insights

### Advanced Features
- **🎯 Emotion Radar**: Multi-dimensional visualization of learning emotions
- **📈 Timeline Tracking**: Historical emotion patterns during learning sessions  
- **🧠 Learning Insights**: AI-powered recommendations based on emotional state
- **⚠️ Smart Interventions**: Automatic alerts when support is needed

## 🎯 Core Components

### Vision AI Engine (`emotion_detector.py`)
- **IBM Watsonx Integration**: LLaMA 90B Vision Model for facial expression analysis
- **Educational Focus**: Specialized prompts for learning-related emotions
- **Robust Processing**: Advanced parsing of AI responses with fallback mechanisms

### Visualization Engine (`emotion_visualizer.py`)
- **Interactive Radar Charts**: Real-time emotion visualization with optimal learning zones
- **Timeline Analytics**: Session progress tracking with trend analysis
- **Professional UI**: Modern design with educational psychology color schemes

### Intervention Engine (`intervention_engine.py`)
- **Evidence-Based Strategies**: Educational psychology principles for learning interventions
- **Intelligent Timing**: Optimal intervention timing based on urgency and learning phase
- **Personalized Recommendations**: Context-aware suggestions for different learning scenarios

## 🧠 Educational Psychology Foundation

EmoRadar is built on established educational psychology research:

- **Flow State Theory**: Optimal challenge-skill balance detection
- **Cognitive Load Theory**: Monitoring confusion and cognitive overload
- **Self-Efficacy Theory**: Confidence and motivation assessment
- **Affective Learning States**: Emotion-learning performance correlation

## 🔒 Privacy & Security

- **Local Processing**: All emotion analysis happens in real-time without storing personal images
- **Secure API**: IBM Watsonx credentials handled through environment variables
- **No Data Retention**: Camera captures are processed immediately and not saved
- **GDPR Compliant**: Privacy-first approach to educational technology

## 🎓 Use Cases

### Educational Institutions
- **Classroom Monitoring**: Real-time student engagement assessment
- **Online Learning**: Enhanced remote education with emotion awareness
- **Special Needs**: Adaptive learning environments for diverse learners

### Individual Learning
- **Study Optimization**: Personal learning state awareness
- **Skill Development**: Emotional feedback for practice sessions
- **Self-Regulation**: Building metacognitive learning skills

## 🚀 Development

### Adding New Features

1. **Core Logic**: Extend modules in main directory
2. **Visualizations**: Enhance `emotion_visualizer.py` components
3. **AI Models**: Modify `emotion_detector.py` for different vision models

### Customization Options

- **Emotion Categories**: Modify emotional dimensions in the detector
- **Visualization Styles**: Update color schemes and chart types
- **Intervention Strategies**: Customize educational recommendations

## 📊 Technical Specifications

- **AI Model**: meta-llama/llama-3-2-90b-vision-instruct
- **Processing**: Real-time facial expression analysis
- **Accuracy**: Educational emotion recognition optimized for learning contexts
- **Performance**: Sub-second analysis with professional UI responsiveness

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues, questions, or feature requests:

1. Check the [Issues](https://github.com/JesseChan5171/EmoRadar/issues) page
2. Review the documentation above
3. Contact the development team

## 🏆 Acknowledgments

- **IBM Watsonx AI**: For providing advanced vision AI capabilities
- **Educational Psychology Research**: Foundation for intervention strategies
- **Streamlit Community**: For the excellent web framework
- **Open Source Contributors**: For inspiration and best practices

---

**Built with ❤️ using IBM Watsonx Vision AI and Educational Psychology Principles**

*Empowering learners through intelligent emotion awareness and personalized educational support.*