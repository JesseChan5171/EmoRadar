"""
🎯 EmoRadar - Core Vision AI Engine

Ultra-focused emotion detection system using IBM Watsonx meta-llama/llama-3-2-90b-vision-instruct
to analyze student emotions in real-time learning scenarios.

Advanced facial expression analysis for educational applications.
Built with IBM Watsonx Vision AI.

Author: Jesse Chan
Repository: https://github.com/JesseChan5171/EmoRadar
"""

import os
import base64
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters


class LearningEmotionDetector:
    """Ultra-focused vision AI system for detecting learning emotions in real-time."""
    
    def __init__(self):
        """Initialize the emotion detector with IBM Watsonx credentials."""
        # Load environment variables
        load_dotenv()
        
        # Get credentials from environment
        self.api_key = os.getenv('WATSONX_API_KEY')
        self.project_id = os.getenv('WATSONX_PROJECT_ID')
        
        if not self.api_key or not self.project_id:
            raise ValueError(
                "WATSONX_API_KEY and WATSONX_PROJECT_ID must be set in .env file"
            )
        
        # Initialize IBM Watsonx credentials
        self.credentials = Credentials(
            url="https://us-south.ml.cloud.ibm.com",
            api_key=self.api_key,
        )
        
        # Configure model parameters for emotion detection
        self.params = TextChatParameters(
            temperature=0.1,  # Low temperature for consistent emotion analysis
            max_tokens=200,   # Sufficient for structured JSON response
        )
        
        # Initialize the vision model
        self.model = ModelInference(
            model_id="meta-llama/llama-3-2-90b-vision-instruct",
            credentials=self.credentials,
            project_id=self.project_id,
            params=self.params
        )
    
    def encode_image(self, image_bytes: bytes) -> str:
        """Encode image bytes to base64 string for model input."""
        return base64.b64encode(image_bytes).decode('utf-8')
    
    def detect_emotions(self, image_base64: str) -> Dict[str, Any]:
        """
        Analyze student image for learning-related emotions using vision AI.
        
        Args:
            image_base64: Base64 encoded image string
            
        Returns:
            Dict containing emotion scores (0-10) and intervention recommendations
        """
        
        # Ultra-focused prompt for learning emotion detection
        emotion_prompt = """
        You are an expert educational psychologist analyzing a student's emotional state during learning.
        
        Analyze this student's facial expression, body language, and overall demeanor for learning-specific emotions.
        
        Focus on these key learning emotions:
        - Frustration: Signs of difficulty, tension, negative emotions
        - Confusion: Puzzled expressions, uncertainty, cognitive struggle  
        - Engagement: Active attention, focus, positive involvement
        - Excitement: Enthusiasm, discovery, breakthrough moments
        - Confidence: Self-assured posture, relaxed competence
        
        Output ONLY a valid JSON object with this exact structure:
        {
            "frustration": 0-10,
            "confusion": 0-10,
            "engagement": 0-10,
            "excitement": 0-10,
            "confidence": 0-10,
            "intervention_needed": true or false,
            "suggested_action": "brief specific recommendation",
            "emotional_state": "one word summary",
            "learning_readiness": 0-10
        }
        
        Be precise and educational psychology-informed in your analysis.
        """
        
        # Build messages payload following IBM Watsonx pattern
        messages = [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": emotion_prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }]
        
        try:
            # Call the vision model
            response = self.model.chat(messages=messages)
            
            # Extract content from response
            content = response["choices"][0]["message"]["content"]
            
            # Parse JSON response
            emotion_data = json.loads(content)
            
            # Validate and enhance the response
            return self._validate_and_enhance_emotions(emotion_data)
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Raw response: {content}")
            return self._get_fallback_emotions()
            
        except Exception as e:
            print(f"Emotion detection error: {e}")
            return self._get_fallback_emotions()
    
    def _validate_and_enhance_emotions(self, emotion_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate emotion data and add calculated insights."""
        
        # Ensure all required fields exist with defaults
        required_fields = {
            'frustration': 5.0,
            'confusion': 5.0, 
            'engagement': 5.0,
            'excitement': 5.0,
            'confidence': 5.0,
            'intervention_needed': False,
            'suggested_action': 'Continue monitoring',
            'emotional_state': 'neutral',
            'learning_readiness': 5.0
        }
        
        for field, default in required_fields.items():
            if field not in emotion_data:
                emotion_data[field] = default
        
        # Calculate composite learning metrics
        emotion_data['overall_wellbeing'] = (
            emotion_data['engagement'] + 
            emotion_data['confidence'] + 
            emotion_data['excitement'] -
            emotion_data['frustration'] -
            emotion_data['confusion']
        ) / 5.0
        
        # Determine intervention priority
        high_frustration = emotion_data['frustration'] > 7
        high_confusion = emotion_data['confusion'] > 8
        low_engagement = emotion_data['engagement'] < 3
        
        if high_frustration or high_confusion or low_engagement:
            emotion_data['intervention_needed'] = True
            emotion_data['intervention_priority'] = 'high'
        elif emotion_data['frustration'] > 5 or emotion_data['confusion'] > 6:
            emotion_data['intervention_priority'] = 'medium'
        else:
            emotion_data['intervention_priority'] = 'low'
        
        return emotion_data
    
    def _get_fallback_emotions(self) -> Dict[str, Any]:
        """Return neutral emotions when detection fails."""
        return {
            'frustration': 5.0,
            'confusion': 5.0,
            'engagement': 5.0,
            'excitement': 5.0,
            'confidence': 5.0,
            'intervention_needed': False,
            'suggested_action': 'Unable to analyze - please ensure clear image',
            'emotional_state': 'unknown',
            'learning_readiness': 5.0,
            'overall_wellbeing': 0.0,
            'intervention_priority': 'low'
        }
    
    def analyze_image_file(self, image_path: str) -> Dict[str, Any]:
        """Convenience method to analyze emotions from image file."""
        try:
            with open(image_path, 'rb') as image_file:
                image_base64 = self.encode_image(image_file.read())
                return self.detect_emotions(image_base64)
        except Exception as e:
            print(f"Error reading image file: {e}")
            return self._get_fallback_emotions()


# Quick test function for development
if __name__ == "__main__":
    print("🎯 Testing Learning Emotion Detector...")
    
    try:
        detector = LearningEmotionDetector()
        print("✅ Emotion detector initialized successfully!")
        
        # Test with sample data
        print("\n📊 Ready to analyze student emotions in real-time!")
        
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        print("Make sure your .env file contains WATSONX_API_KEY and WATSONX_PROJECT_ID")