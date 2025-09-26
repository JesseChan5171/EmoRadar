"""
🎯 EmoRadar - Ultra Visualization Engine

Advanced emotion visualization system with radar charts, timelines, and intervention alerts
for real-time learning emotion monitoring.

Features ultra-cool radar visualizations and learning analytics dashboards.

Author: Jesse Chan
Repository: https://github.com/JesseChan5171/EmoRadar
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from typing import Dict, List, Any
import pandas as pd
import numpy as np


class EmotionVisualizer:
    """Ultra-advanced visualization system for learning emotions."""
    
    def __init__(self):
        """Initialize the emotion visualizer."""
        self.color_scheme = {
            'engagement': '#32C997',    # Green - positive
            'confidence': '#4A90E2',    # Blue - stable
            'excitement': '#F39C12',    # Orange - energetic
            'confusion': '#E74C3C',     # Red - concerning
            'frustration': '#8E44AD',   # Purple - warning
            'optimal_zone': 'rgba(100, 100, 100, 0.3)'
        }
    
    def render_emotion_radar(self, emotion_data: Dict[str, Any], container=None) -> None:
        """
        Create ultra-cool radar chart for real-time emotion visualization.
        
        Args:
            emotion_data: Dictionary with emotion scores (0-10)
            container: Streamlit container to render in (optional)
        """
        
        # Prepare data for radar chart
        emotions = ['Engagement', 'Confidence', 'Excitement', 'Clarity', 'Calm']
        
        # Convert confusion and frustration to positive metrics
        current_values = [
            emotion_data.get('engagement', 5),
            emotion_data.get('confidence', 5),
            emotion_data.get('excitement', 5),
            10 - emotion_data.get('confusion', 5),  # Clarity = inverse of confusion
            10 - emotion_data.get('frustration', 5)  # Calm = inverse of frustration
        ]
        
        # Optimal learning zone ranges
        optimal_values = [8, 7, 6, 8, 8]  # Ideal ranges for each emotion
        
        # Create radar chart
        fig = go.Figure()
        
        # Add optimal learning zone
        fig.add_trace(go.Scatterpolar(
            r=optimal_values + [optimal_values[0]],  # Close the polygon
            theta=emotions + [emotions[0]],
            fill='toself',
            name='Optimal Learning Zone',
            line=dict(color='rgba(128, 128, 128, 0.8)', width=2, dash='dash'),
            fillcolor='rgba(128, 128, 128, 0.1)',
            opacity=0.7,
            hovertemplate='<b>%{theta}</b><br>Optimal: %{r}/10<extra></extra>'
        ))
        
        # Add current emotions
        fig.add_trace(go.Scatterpolar(
            r=current_values + [current_values[0]],  # Close the polygon
            theta=emotions + [emotions[0]],
            fill='toself',
            name='Current State',
            line=dict(color='#32C997', width=3),
            fillcolor='rgba(50, 201, 151, 0.3)',
            hovertemplate='<b>%{theta}</b><br>Current: %{r}/10<extra></extra>'
        ))
        
        # Customize layout for ultra appearance
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10],
                    tickfont=dict(size=12),
                    gridcolor='rgba(128, 128, 128, 0.3)',
                    linecolor='rgba(128, 128, 128, 0.3)'
                ),
                angularaxis=dict(
                    tickfont=dict(size=14, color='#2E3440'),
                    gridcolor='rgba(128, 128, 128, 0.3)',
                    linecolor='rgba(128, 128, 128, 0.3)'
                )
            ),
            showlegend=True,
            legend=dict(
                x=0.02,
                y=0.98,
                bgcolor='rgba(255, 255, 255, 0.8)',
                bordercolor='rgba(128, 128, 128, 0.3)',
                borderwidth=1
            ),
            title=dict(
                text="🎯 Learning Emotion Radar",
                x=0.5,
                font=dict(size=18, color='#2E3440')
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=450,
            margin=dict(t=80, b=20, l=20, r=20)
        )
        
        # Render in container or default
        if container:
            container.plotly_chart(fig, use_container_width=True)
        else:
            st.plotly_chart(fig, use_container_width=True)
    
    def render_emotion_metrics(self, emotion_data: Dict[str, Any]) -> None:
        """Render emotion metrics with ultra styling."""
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Overall wellbeing score
        wellbeing = emotion_data.get('overall_wellbeing', 0)
        wellbeing_color = 'normal' if wellbeing > 0 else 'inverse'
        
        with col1:
            st.metric(
                "🎯 Learning Readiness",
                f"{emotion_data.get('learning_readiness', 5):.1f}/10",
                delta=None
            )
        
        with col2:
            st.metric(
                "💚 Overall Wellbeing", 
                f"{wellbeing:+.1f}",
                delta=None
            )
        
        with col3:
            intervention = "🚨 HIGH" if emotion_data.get('intervention_needed') else "✅ LOW"
            st.metric(
                "⚡ Intervention Priority",
                emotion_data.get('intervention_priority', 'low').upper(),
                delta=None
            )
        
        with col4:
            st.metric(
                "🧠 Emotional State",
                emotion_data.get('emotional_state', 'unknown').title(),
                delta=None
            )
    
    def render_intervention_alert(self, emotion_data: Dict[str, Any]) -> None:
        """Render ultra-styled intervention alerts."""
        
        if emotion_data.get('intervention_needed', False):
            priority = emotion_data.get('intervention_priority', 'medium')
            suggestion = emotion_data.get('suggested_action', 'Monitor student closely')
            
            if priority == 'high':
                st.error(f"🚨 **IMMEDIATE INTERVENTION NEEDED**\n\n{suggestion}")
            elif priority == 'medium':
                st.warning(f"⚠️ **ATTENTION RECOMMENDED**\n\n{suggestion}")
            else:
                st.info(f"💡 **SUGGESTION**\n\n{suggestion}")
        else:
            st.success("✅ **STUDENT ON TRACK** - Emotions indicate good learning state")
    
    def render_emotion_timeline(self, emotion_history: List[Dict]) -> None:
        """Render emotion timeline showing changes over learning session."""
        
        if not emotion_history or len(emotion_history) < 2:
            st.info("📊 Emotion timeline will appear after multiple readings...")
            return
        
        # Convert to DataFrame
        df = pd.DataFrame(emotion_history)
        
        if 'timestamp' not in df.columns:
            # Add timestamps if missing
            df['timestamp'] = pd.date_range(
                start=datetime.now() - timedelta(minutes=len(df)*2),
                periods=len(df),
                freq='2min'
            )
        
        # Create timeline chart
        fig = go.Figure()
        
        emotions = ['engagement', 'confidence', 'excitement', 'confusion', 'frustration']
        colors = ['#32C997', '#4A90E2', '#F39C12', '#E74C3C', '#8E44AD']
        
        for emotion, color in zip(emotions, colors):
            if emotion in df.columns:
                fig.add_trace(go.Scatter(
                    x=df['timestamp'],
                    y=df[emotion],
                    mode='lines+markers',
                    name=emotion.title(),
                    line=dict(color=color, width=2),
                    marker=dict(size=6),
                    hovertemplate=f'<b>{emotion.title()}</b><br>Time: %{{x}}<br>Level: %{{y}}/10<extra></extra>'
                ))
        
        fig.update_layout(
            title="📈 Emotion Timeline - Learning Session Progress",
            xaxis_title="Time",
            yaxis_title="Emotion Level (0-10)",
            yaxis=dict(range=[0, 10]),
            height=300,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(t=60, b=40, l=40, r=40)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_learning_insights(self, emotion_data: Dict[str, Any]) -> None:
        """Render ultra learning insights and recommendations."""
        
        st.markdown("### 🧠 Learning Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Current Learning State:**")
            
            # Determine learning phase based on emotions
            high_confusion = emotion_data.get('confusion', 5) > 7
            high_engagement = emotion_data.get('engagement', 5) > 7
            high_excitement = emotion_data.get('excitement', 5) > 7
            high_frustration = emotion_data.get('frustration', 5) > 7
            
            if high_excitement and high_engagement:
                st.success("🎉 **Discovery Mode** - Student having breakthrough moments!")
            elif high_confusion and high_engagement:
                st.info("🤔 **Deep Processing** - Student actively working through challenges")
            elif high_frustration:
                st.error("😤 **Struggle Phase** - Student needs support or break")
            elif high_engagement:
                st.success("🎯 **Flow State** - Optimal learning conditions")
            else:
                st.info("😐 **Neutral State** - Standard learning progress")
        
        with col2:
            st.markdown("**Recommendations:**")
            
            recommendations = []
            
            if emotion_data.get('engagement', 5) < 4:
                recommendations.append("🎮 Add interactive elements to boost engagement")
            
            if emotion_data.get('confusion', 5) > 7:
                recommendations.append("📚 Provide additional examples or simpler explanations")
            
            if emotion_data.get('frustration', 5) > 6:
                recommendations.append("☕ Suggest a short break or change of activity")
            
            if emotion_data.get('confidence', 5) < 4:
                recommendations.append("💪 Offer encouragement and celebrate small wins")
            
            if not recommendations:
                recommendations.append("✅ Continue current approach - student doing well!")
            
            for rec in recommendations[:3]:  # Show top 3 recommendations
                st.write(f"• {rec}")


# Utility functions for session management
def initialize_emotion_session():
    """Initialize session state for emotion tracking."""
    if 'emotion_history' not in st.session_state:
        st.session_state.emotion_history = []
    
    if 'session_start_time' not in st.session_state:
        st.session_state.session_start_time = datetime.now()

def add_emotion_reading(emotion_data: Dict[str, Any]):
    """Add new emotion reading to session history."""
    emotion_data_with_time = emotion_data.copy()
    emotion_data_with_time['timestamp'] = datetime.now()
    
    st.session_state.emotion_history.append(emotion_data_with_time)
    
    # Keep only last 20 readings to prevent memory issues
    if len(st.session_state.emotion_history) > 20:
        st.session_state.emotion_history = st.session_state.emotion_history[-20:]