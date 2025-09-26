#!/usr/bin/env python3
"""
🎯 EmoRadar - Real-Time Learning Emotion Detection

Advanced emotion analysis system using IBM Watsonx Vision AI for educational applications.
Features real-time facial expression analysis, learning emotion recognition, and intelligent
intervention recommendations based on educational psychology principles.

Author: Jesse Chan
Repository: https://github.com/JesseChan5171/EmoRadar
"""

import streamlit as st
import base64
import json
import re
from datetime import datetime
from emotion_detector import LearningEmotionDetector
import plotly.graph_objects as go

def parse_descriptive_response(content):
    """Parse LLM descriptive response into structured emotion data."""
    emotion_data = {
        'frustration': 5, 'confusion': 5, 'engagement': 5, 
        'excitement': 5, 'confidence': 5, 'learning_readiness': 5,
        'intervention_needed': False, 'suggested_action': 'Continue learning',
        'emotional_state': 'analyzing'
    }
    
    # Flexible patterns to extract emotion scores
    patterns = {
        'frustration': [r'frustration[^\d]*(\d+)[/:]?\s*(?:out of\s*)?10', r'\*\*frustration[^\d]*(\d+)/10'],
        'confusion': [r'confusion[^\d]*(\d+)[/:]?\s*(?:out of\s*)?10', r'\*\*confusion[^\d]*(\d+)/10'],
        'engagement': [r'engagement[^\d]*(\d+)[/:]?\s*(?:out of\s*)?10', r'\*\*engagement[^\d]*(\d+)/10'],
        'excitement': [r'excitement[^\d]*(\d+)[/:]?\s*(?:out of\s*)?10', r'\*\*excitement[^\d]*(\d+)/10'],
        'confidence': [r'confidence[^\d]*(\d+)[/:]?\s*(?:out of\s*)?10', r'\*\*confidence[^\d]*(\d+)/10'],
        'learning_readiness': [r'learning readiness[^\d]*(\d+)[/:]?\s*(?:out of\s*)?10', r'readiness[^\d]*(\d+)/10']
    }
    
    extracted_emotions = {}
    
    for emotion, pattern_list in patterns.items():
        for pattern in pattern_list:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                value = int(match.group(1))
                emotion_data[emotion] = value
                extracted_emotions[emotion] = value
                break
    
    # Detect intervention needs
    intervention_keywords = ['intervention needed', 'needs support', 'requires help', 'struggling']
    for keyword in intervention_keywords:
        if keyword in content.lower():
            emotion_data['intervention_needed'] = True
            break
    
    # Extract suggested actions
    action_patterns = [
        r'suggested action[:\s]*["\']?([^"\'.\n]{10,100})["\']?',
        r'recommendation[:\s]*["\']?([^"\'.\n]{10,100})["\']?',
        r'should[:\s]*([^.\n]{10,100})'
    ]
    
    for pattern in action_patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            emotion_data['suggested_action'] = match.group(1).strip()
            break
    
    # Extract emotional state
    state_patterns = [
        r'emotional state[:\s]*["\']?([a-zA-Z\s]{3,20})["\']?',
        r'state[:\s]*["\']?([a-zA-Z\s]{3,20})["\']?',
        r'appears?\s+([\w\s]{5,20})(?:\s+but|\s+and|\.|\n)'
    ]
    
    for pattern in state_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            state = match.group(1).strip().lower()
            if len(state.split()) <= 3:
                emotion_data['emotional_state'] = state
                break
    
    return emotion_data, extracted_emotions

# Configure Streamlit page
st.set_page_config(
    page_title="🎯 EmoRadar - Real-Time Learning Emotion Detection",
    page_icon="🎯",
    layout="wide",
    menu_items={
        'Get Help': 'https://github.com/JesseChan5171/EmoRadar',
        'Report a bug': 'https://github.com/JesseChan5171/EmoRadar/issues',
        'About': """
        # 🎯 EmoRadar
        Real-Time Learning Emotion Detection using IBM Watsonx Vision AI
        
        **Features:**
        - Advanced facial expression analysis
        - Educational psychology insights
        - Learning intervention recommendations
        - Multi-dimensional emotion visualization
        
        Built with IBM Watsonx • LLaMA Vision Models • Streamlit
        """
    }
)

# Enhanced CSS styling
st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 15px;
    color: white;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}
.extraction-box {
    background: #e8f4fd;
    border: 2px solid #2196F3;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}
.success-extraction {
    background: #e8f5e8;
    border: 2px solid #4CAF50;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}
.metric-card {
    background: white;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🎯 EmoRadar</h1>
    <p>Real-Time Learning Emotion Detection with IBM Watsonx Vision AI</p>
    <p><small>Advanced Educational Psychology Intelligence • LLaMA 90B Vision Model</small></p>
</div>
""", unsafe_allow_html=True)

# Initialize emotion detector
@st.cache_resource
def get_detector():
    """Initialize the emotion detection system."""
    try:
        detector = LearningEmotionDetector()
        return detector, True
    except Exception as e:
        st.error(f"❌ Failed to initialize emotion detector: {e}")
        st.info("Please check your IBM Watsonx credentials in the .env file")
        return None, False

detector, detector_ready = get_detector()

if not detector_ready:
    st.error("🚫 Emotion detection system not available")
    st.info("To set up EmoRadar:")
    st.code("""
# 1. Copy environment template
cp .env.example .env

# 2. Edit .env with your IBM Watsonx credentials
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here

# 3. Restart the application
streamlit run app.py
    """)
    st.stop()

def analyze_emotions(detector, image_base64):
    """Analyze student emotions using IBM Watsonx Vision AI."""
    
    # Optimized prompt for educational emotion analysis
    emotion_prompt = """Analyze this student's facial expression and body language for learning-related emotions.

Please rate each emotion from 0-10 based on what you observe:

- Frustration (signs of difficulty, tension): 
- Confusion (puzzled, uncertain expression):
- Engagement (focused, attentive):
- Excitement (enthusiastic, interested):
- Confidence (self-assured, relaxed):
- Learning Readiness (overall readiness to learn):

Also determine:
- Does this student need intervention or support?
- What's their current emotional state?
- What would help them learn more effectively?

Provide specific numerical ratings and observations."""

    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": emotion_prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
        ]
    }]
    
    response = detector.model.chat(messages=messages)
    content = response["choices"][0]["message"]["content"].strip()
    
    return content, response

# Main application interface
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("📹 Student Monitoring")
    
    st.markdown("""
    **Instructions:**
    1. Position yourself clearly in the camera frame
    2. Ensure good lighting on your face
    3. Click to capture your current learning state
    4. View real-time emotion analysis results
    """)
    
    camera_input = st.camera_input("Capture image for emotion analysis")
    
    if camera_input is not None:
        st.image(camera_input, caption="Analyzing emotions...", width=300)

with col2:
    st.subheader("🎯 Emotion Analysis Results")
    
    if camera_input is not None:
        with st.spinner("🧠 Analyzing with IBM Watsonx Vision AI..."):
            try:
                # Process captured image
                image_bytes = camera_input.read()
                image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                
                # Perform emotion analysis
                content, raw_response = analyze_emotions(detector, image_base64)
                
                st.success("✅ Vision AI Analysis Complete!")
                
                # Show AI analysis details
                with st.expander("🔍 AI Analysis Details"):
                    st.write(content)
                
                # Parse emotions from response
                emotion_data, extracted_emotions = parse_descriptive_response(content)
                
                # Display extraction results
                if extracted_emotions:
                    st.markdown('<div class="success-extraction">✅ <strong>Successfully Extracted Emotions!</strong></div>', unsafe_allow_html=True)
                    
                    cols = st.columns(3)
                    for i, (emotion, value) in enumerate(extracted_emotions.items()):
                        with cols[i % 3]:
                            st.metric(f"🎯 {emotion.replace('_', ' ').title()}", f"{value}/10")
                else:
                    st.markdown('<div class="extraction-box">🔧 <strong>Using Enhanced Parsing...</strong></div>', unsafe_allow_html=True)
                
                # Create emotion radar visualization
                st.subheader("🎯 Learning Emotion Radar")
                
                categories = ['Engagement', 'Confidence', 'Excitement', 'Clarity', 'Calm']
                values = [
                    emotion_data.get('engagement', 5),
                    emotion_data.get('confidence', 5), 
                    emotion_data.get('excitement', 5),
                    10 - emotion_data.get('confusion', 5),  # Invert to clarity
                    10 - emotion_data.get('frustration', 5)  # Invert to calm
                ]
                
                # Build radar chart
                fig = go.Figure()
                
                # Current emotions
                fig.add_trace(go.Scatterpolar(
                    r=values + [values[0]],
                    theta=categories + [categories[0]],
                    fill='toself',
                    name='Current State',
                    line=dict(color='#FF6B6B', width=4),
                    fillcolor='rgba(255, 107, 107, 0.3)'
                ))
                
                # Optimal learning zone
                optimal = [8, 7, 6, 8, 8]
                fig.add_trace(go.Scatterpolar(
                    r=optimal + [optimal[0]],
                    theta=categories + [categories[0]],
                    fill='toself',
                    name='Optimal Zone',
                    line=dict(color='rgba(74, 222, 128, 0.8)', width=2, dash='dot'),
                    fillcolor='rgba(74, 222, 128, 0.1)'
                ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True, 
                            range=[0, 10],
                            tickfont=dict(size=12)
                        )
                    ),
                    showlegend=True,
                    title="Real-Time Learning Emotion Analysis",
                    height=450,
                    font=dict(size=14)
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Detailed emotion metrics
                st.subheader("📊 Emotion Metrics")
                
                col1_metrics, col2_metrics, col3_metrics = st.columns(3)
                
                with col1_metrics:
                    st.metric("🎯 Learning Readiness", f"{emotion_data.get('learning_readiness', 5)}/10")
                    st.metric("⚡ Engagement", f"{emotion_data.get('engagement', 5)}/10")
                
                with col2_metrics:
                    st.metric("💪 Confidence", f"{emotion_data.get('confidence', 5)}/10")
                    st.metric("🎉 Excitement", f"{emotion_data.get('excitement', 5)}/10")
                
                with col3_metrics:
                    st.metric("🤔 Confusion Level", f"{emotion_data.get('confusion', 5)}/10")
                    st.metric("😤 Frustration Level", f"{emotion_data.get('frustration', 5)}/10")
                
                # Learning recommendations
                st.subheader("🧠 Learning Recommendations")
                
                if emotion_data.get('intervention_needed', False):
                    suggestion = emotion_data.get('suggested_action', 'Consider taking a break or seeking additional support')
                    st.warning(f"⚠️ **Intervention Recommended:** {suggestion}")
                else:
                    st.success("✅ **Optimal Learning State** - Continue your current approach!")
                
                # Current state summary
                emotional_state = emotion_data.get('emotional_state', 'focused')
                st.info(f"🧠 **Current State:** {emotional_state.title()}")
                
                # Personalized learning insights
                st.subheader("💡 Personalized Insights")
                
                insights = []
                if emotion_data.get('engagement', 5) >= 7:
                    insights.append("🎯 High engagement detected - excellent focus for learning!")
                if emotion_data.get('confusion', 5) >= 7:
                    insights.append("🤔 Significant confusion - consider reviewing prerequisites")
                if emotion_data.get('frustration', 5) >= 6:
                    insights.append("😤 Elevated frustration - a short break might be beneficial")
                if emotion_data.get('excitement', 5) >= 7:
                    insights.append("🎉 Great enthusiasm - leverage this motivation!")
                if emotion_data.get('confidence', 5) <= 3:
                    insights.append("💪 Low confidence - try starting with simpler concepts")
                
                if not insights:
                    insights.append("📚 Balanced emotional state - maintain current learning approach")
                
                for insight in insights:
                    st.write(f"• {insight}")
                
            except Exception as e:
                st.error(f"❌ Emotion analysis failed: {e}")
                st.info("This may be due to API limits, network issues, or image quality. Please try again.")
    
    else:
        st.info("📷 Capture an image above to begin emotion analysis")
        
        # Demo visualization
        st.subheader("🎯 Sample Emotion Radar")
        demo_fig = go.Figure()
        
        demo_categories = ['Engagement', 'Confidence', 'Excitement', 'Clarity', 'Calm']
        demo_values = [6, 5, 4, 6, 7]
        
        demo_fig.add_trace(go.Scatterpolar(
            r=demo_values + [demo_values[0]],
            theta=demo_categories + [demo_categories[0]],
            fill='toself',
            name='Sample Analysis',
            line=dict(color='#888888', width=2),
            fillcolor='rgba(136, 136, 136, 0.2)'
        ))
        
        demo_fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=True,
            title="Awaiting Your Analysis...",
            height=400
        )
        
        st.plotly_chart(demo_fig, use_container_width=True)

# Sidebar information
st.sidebar.success("✅ IBM Watsonx Vision AI: Connected")
st.sidebar.info("🤖 Model: meta-llama/llama-3-2-90b-vision-instruct")
st.sidebar.info("🎯 Status: Real-Time Analysis Ready")

st.sidebar.header("🎯 About EmoRadar")
st.sidebar.markdown("""
**EmoRadar** is an advanced emotion detection system designed for educational environments. 

**Key Features:**
- **Real-time analysis** of learning emotions
- **Educational psychology** insights
- **Personalized recommendations** for optimal learning
- **Multi-dimensional visualization** of emotional states
- **Professional intervention** guidelines

**Technology Stack:**
- IBM Watsonx AI Platform
- LLaMA 90B Vision Model
- Streamlit Web Framework
- Advanced Computer Vision
""")

st.sidebar.header("📚 How to Use")
st.sidebar.markdown("""
1. **📸 Capture Image**: Use the camera input to take your photo
2. **🤖 AI Analysis**: Wait for IBM Watsonx to analyze your expressions
3. **📊 View Results**: See your emotion radar and detailed metrics
4. **💡 Get Insights**: Receive personalized learning recommendations
5. **🎯 Optimize**: Use insights to improve your learning experience
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🎯 <strong>EmoRadar</strong> - Real-Time Learning Emotion Detection</p>
    <p>Powered by IBM Watsonx AI • Built for Educational Excellence</p>
    <p><a href="https://github.com/JesseChan5171/EmoRadar" target="_blank">GitHub Repository</a> • 
    <a href="https://github.com/JesseChan5171/EmoRadar/issues" target="_blank">Report Issues</a></p>
</div>
""", unsafe_allow_html=True)