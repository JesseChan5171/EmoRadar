"""
🎯 EmoRadar - Ultra Intervention Engine

Intelligent intervention system that provides personalized learning recommendations
based on real-time emotion analysis and educational psychology principles.

Features smart intervention timing, personalized strategies, and learning science-backed recommendations.

Author: Jesse Chan
Repository: https://github.com/JesseChan5171/EmoRadar
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from enum import Enum
import random


class InterventionType(Enum):
    """Types of learning interventions available."""
    IMMEDIATE = "immediate"     # Stop current activity
    ADAPTIVE = "adaptive"       # Modify current approach
    SUPPORTIVE = "supportive"   # Provide additional support
    MOTIVATIONAL = "motivational"  # Boost confidence/engagement
    COGNITIVE = "cognitive"     # Address cognitive load


class LearningPhase(Enum):
    """Different phases of learning that affect intervention strategies."""
    INTRODUCTION = "introduction"   # First exposure to concept
    PRACTICE = "practice"          # Skill development
    APPLICATION = "application"    # Real-world usage
    ASSESSMENT = "assessment"      # Testing understanding
    REVIEW = "review"             # Reinforcement


class InterventionEngine:
    """Ultra-intelligent intervention system for adaptive learning support."""
    
    def __init__(self):
        """Initialize the intervention engine with learning science principles."""
        
        # Intervention strategies database
        self.intervention_strategies = {
            'high_frustration': {
                InterventionType.IMMEDIATE: [
                    "Take a 5-minute mindful breathing break",
                    "Step away and do light physical activity",
                    "Switch to a completely different subject for 10 minutes",
                    "Talk through the problem out loud or with someone"
                ],
                InterventionType.ADAPTIVE: [
                    "Break the current problem into smaller, manageable steps",
                    "Use visual aids or diagrams to represent the concept",
                    "Find real-world analogies that relate to your experience",
                    "Try working backwards from the solution"
                ],
                InterventionType.SUPPORTIVE: [
                    "Access additional examples of similar problems",
                    "Watch explanatory videos on the topic",
                    "Join a study group or find a learning partner",
                    "Schedule time with a tutor or instructor"
                ]
            },
            
            'high_confusion': {
                InterventionType.COGNITIVE: [
                    "Create a concept map to organize related ideas",
                    "Write a summary of what you do understand so far",
                    "Identify specific points of confusion to focus on",
                    "Use the 'explain it to a 5-year-old' technique"
                ],
                InterventionType.ADAPTIVE: [
                    "Return to prerequisite concepts and review",
                    "Approach the topic from a different angle or method",
                    "Use multiple learning modalities (visual, audio, kinesthetic)",
                    "Practice with easier examples before tackling hard ones"
                ],
                InterventionType.SUPPORTIVE: [
                    "Seek clarification on confusing terminology",
                    "Find additional resources with different explanations",
                    "Ask specific questions rather than 'I don't get it'",
                    "Work with examples that build complexity gradually"
                ]
            },
            
            'low_engagement': {
                InterventionType.MOTIVATIONAL: [
                    "Connect the material to your personal interests or goals",
                    "Set small, achievable milestones with rewards",
                    "Find the 'why' behind what you're learning",
                    "Challenge yourself with a fun, related puzzle"
                ],
                InterventionType.ADAPTIVE: [
                    "Switch to more interactive learning methods",
                    "Incorporate gamification or competition elements",
                    "Use multimedia content (videos, podcasts, apps)",
                    "Apply learning through hands-on projects"
                ],
                InterventionType.SUPPORTIVE: [
                    "Study with peers or in a group setting",
                    "Change your learning environment for freshness",
                    "Set shorter study sessions with clear objectives",
                    "Track progress visually to see improvement"
                ]
            },
            
            'low_confidence': {
                InterventionType.MOTIVATIONAL: [
                    "Review recent successes and progress made",
                    "Start with easier problems to build momentum",
                    "Focus on effort and improvement rather than perfection",
                    "Remind yourself that struggle is part of learning"
                ],
                InterventionType.SUPPORTIVE: [
                    "Practice positive self-talk and growth mindset",
                    "Break challenges into very small, manageable pieces",
                    "Celebrate small wins and incremental progress",
                    "Seek encouragement from mentors or study partners"
                ],
                InterventionType.ADAPTIVE: [
                    "Use scaffolding techniques with guided practice",
                    "Work with templates or structured approaches",
                    "Practice similar problems before trying new ones",
                    "Build confidence with mastery-based learning"
                ]
            },
            
            'optimal_state': {
                InterventionType.ADAPTIVE: [
                    "Increase challenge level to maintain optimal difficulty",
                    "Explore advanced applications of current concepts",
                    "Teach the concept to someone else to deepen understanding",
                    "Connect current learning to broader knowledge network"
                ],
                InterventionType.SUPPORTIVE: [
                    "Document insights and breakthrough moments",
                    "Apply learning to creative or novel problems",
                    "Explore related topics that spark curiosity",
                    "Prepare to help others who might be struggling"
                ]
            }
        }
        
        # Context-specific modifications based on learning phase
        self.phase_modifiers = {
            LearningPhase.INTRODUCTION: {
                'focus': 'building foundation',
                'patience_level': 'high',
                'complexity_reduction': 'maximum'
            },
            LearningPhase.PRACTICE: {
                'focus': 'skill development',
                'patience_level': 'medium',
                'complexity_reduction': 'moderate'
            },
            LearningPhase.APPLICATION: {
                'focus': 'real-world connection',
                'patience_level': 'medium',
                'complexity_reduction': 'minimal'
            },
            LearningPhase.ASSESSMENT: {
                'focus': 'performance optimization',
                'patience_level': 'low',
                'complexity_reduction': 'none'
            }
        }
    
    def analyze_intervention_need(self, emotion_data: Dict[str, Any], 
                                 learning_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze current emotional state and determine intervention requirements.
        
        Args:
            emotion_data: Current emotion scores and state
            learning_context: Optional context about current learning activity
            
        Returns:
            Comprehensive intervention analysis and recommendations
        """
        
        # Extract key emotional indicators
        frustration = emotion_data.get('frustration', 5)
        confusion = emotion_data.get('confusion', 5)
        engagement = emotion_data.get('engagement', 5)
        confidence = emotion_data.get('confidence', 5)
        excitement = emotion_data.get('excitement', 5)
        
        # Determine primary emotional concern
        primary_concern = self._identify_primary_concern(emotion_data)
        
        # Determine intervention urgency
        urgency = self._calculate_intervention_urgency(emotion_data)
        
        # Get learning phase context
        current_phase = learning_context.get('phase', LearningPhase.PRACTICE) if learning_context else LearningPhase.PRACTICE
        
        # Generate specific interventions
        interventions = self._generate_interventions(primary_concern, urgency, current_phase)
        
        # Calculate optimal intervention timing
        timing = self._calculate_intervention_timing(emotion_data, learning_context)
        
        return {
            'primary_concern': primary_concern,
            'urgency_level': urgency,
            'intervention_type': interventions['type'],
            'recommended_actions': interventions['actions'],
            'timing': timing,
            'explanation': interventions['explanation'],
            'success_indicators': interventions['success_indicators'],
            'learning_phase': current_phase,
            'predicted_outcome': self._predict_intervention_outcome(emotion_data, interventions)
        }
    
    def _identify_primary_concern(self, emotion_data: Dict[str, Any]) -> str:
        """Identify the primary emotional concern requiring intervention."""
        
        concerns = []
        
        # Check each emotional dimension
        if emotion_data.get('frustration', 5) > 7:
            concerns.append(('high_frustration', emotion_data['frustration']))
        
        if emotion_data.get('confusion', 5) > 7:
            concerns.append(('high_confusion', emotion_data['confusion']))
        
        if emotion_data.get('engagement', 5) < 4:
            concerns.append(('low_engagement', 10 - emotion_data['engagement']))
        
        if emotion_data.get('confidence', 5) < 4:
            concerns.append(('low_confidence', 10 - emotion_data['confidence']))
        
        # Return highest priority concern
        if concerns:
            return max(concerns, key=lambda x: x[1])[0]
        
        # Check for optimal state
        if (emotion_data.get('engagement', 5) > 7 and 
            emotion_data.get('confidence', 5) > 6 and
            emotion_data.get('frustration', 5) < 4):
            return 'optimal_state'
        
        return 'neutral_state'
    
    def _calculate_intervention_urgency(self, emotion_data: Dict[str, Any]) -> str:
        """Calculate how urgently intervention is needed."""
        
        # Critical indicators
        critical_frustration = emotion_data.get('frustration', 5) > 8
        critical_confusion = emotion_data.get('confusion', 5) > 8
        critical_disengagement = emotion_data.get('engagement', 5) < 2
        
        if critical_frustration or critical_confusion or critical_disengagement:
            return 'critical'
        
        # High priority indicators
        high_frustration = emotion_data.get('frustration', 5) > 6
        high_confusion = emotion_data.get('confusion', 5) > 6
        low_engagement = emotion_data.get('engagement', 5) < 4
        
        if high_frustration or high_confusion or low_engagement:
            return 'high'
        
        # Medium priority indicators
        moderate_concerns = (
            emotion_data.get('frustration', 5) > 4 or
            emotion_data.get('confusion', 5) > 5 or
            emotion_data.get('engagement', 5) < 6 or
            emotion_data.get('confidence', 5) < 5
        )
        
        if moderate_concerns:
            return 'medium'
        
        return 'low'
    
    def _generate_interventions(self, primary_concern: str, urgency: str, 
                               phase: LearningPhase) -> Dict[str, Any]:
        """Generate specific intervention recommendations."""
        
        if primary_concern not in self.intervention_strategies:
            return {
                'type': InterventionType.SUPPORTIVE,
                'actions': ["Continue monitoring student progress"],
                'explanation': "No specific intervention needed at this time",
                'success_indicators': ["Maintained engagement", "Steady progress"]
            }
        
        strategies = self.intervention_strategies[primary_concern]
        
        # Select intervention type based on urgency
        if urgency == 'critical':
            intervention_type = InterventionType.IMMEDIATE
        elif urgency == 'high':
            intervention_type = random.choice([InterventionType.IMMEDIATE, InterventionType.ADAPTIVE])
        elif urgency == 'medium':
            intervention_type = random.choice([InterventionType.ADAPTIVE, InterventionType.SUPPORTIVE])
        else:
            intervention_type = InterventionType.SUPPORTIVE
        
        # Get actions for this intervention type
        if intervention_type in strategies:
            actions = strategies[intervention_type].copy()
        else:
            # Fall back to any available strategy
            available_types = list(strategies.keys())
            intervention_type = available_types[0]
            actions = strategies[intervention_type].copy()
        
        # Randomize action selection
        selected_actions = random.sample(actions, min(2, len(actions)))
        
        # Generate explanation
        explanation = self._generate_intervention_explanation(primary_concern, intervention_type, urgency)
        
        # Define success indicators
        success_indicators = self._define_success_indicators(primary_concern)
        
        return {
            'type': intervention_type,
            'actions': selected_actions,
            'explanation': explanation,
            'success_indicators': success_indicators
        }
    
    def _calculate_intervention_timing(self, emotion_data: Dict[str, Any], 
                                     learning_context: Optional[Dict[str, Any]]) -> Dict[str, str]:
        """Calculate optimal timing for intervention."""
        
        urgency = self._calculate_intervention_urgency(emotion_data)
        
        timing_map = {
            'critical': {
                'when': 'immediately',
                'duration': '5-10 minutes',
                'frequency': 'as needed'
            },
            'high': {
                'when': 'within next 2-3 minutes',
                'duration': '3-5 minutes',
                'frequency': 'monitor every 5 minutes'
            },
            'medium': {
                'when': 'at next natural break',
                'duration': '2-3 minutes',
                'frequency': 'check every 10 minutes'
            },
            'low': {
                'when': 'end of current activity',
                'duration': '1-2 minutes',
                'frequency': 'monitor every 15 minutes'
            }
        }
        
        return timing_map.get(urgency, timing_map['medium'])
    
    def _generate_intervention_explanation(self, concern: str, intervention_type: InterventionType, 
                                          urgency: str) -> str:
        """Generate explanation for why this intervention is recommended."""
        
        explanations = {
            'high_frustration': f"Student showing signs of learning frustration. {intervention_type.value.title()} intervention needed to prevent negative learning spiral.",
            'high_confusion': f"Cognitive confusion detected. {intervention_type.value.title()} support will help clarify concepts and reduce cognitive load.",
            'low_engagement': f"Engagement levels below optimal range. {intervention_type.value.title()} strategies will help re-energize learning process.",
            'low_confidence': f"Confidence indicators suggest student needs encouragement. {intervention_type.value.title()} approach will build self-efficacy.",
            'optimal_state': f"Student in excellent learning state. {intervention_type.value.title()} enhancement will maximize learning potential."
        }
        
        return explanations.get(concern, f"Emotional state analysis suggests {intervention_type.value} intervention would be beneficial.")
    
    def _define_success_indicators(self, concern: str) -> List[str]:
        """Define what successful intervention looks like."""
        
        indicators = {
            'high_frustration': [
                "Decreased facial tension and more relaxed posture",
                "Renewed willingness to attempt problems",
                "Improved emotional regulation"
            ],
            'high_confusion': [
                "Clearer understanding demonstrated through questions",
                "Improved accuracy on practice problems",
                "More confident body language"
            ],
            'low_engagement': [
                "Increased attention and focus on materials", 
                "Active participation in learning activities",
                "Positive emotional responses to content"
            ],
            'low_confidence': [
                "Improved posture and self-assured behavior",
                "Willingness to attempt challenging problems",
                "Positive self-statements about ability"
            ]
        }
        
        return indicators.get(concern, ["Improved overall emotional state", "Better learning engagement"])
    
    def _predict_intervention_outcome(self, emotion_data: Dict[str, Any], 
                                    interventions: Dict[str, Any]) -> Dict[str, Any]:
        """Predict likely outcome of intervention."""
        
        current_state = emotion_data.get('overall_wellbeing', 0)
        intervention_type = interventions['type']
        
        # Predict improvement based on intervention type
        improvement_factors = {
            InterventionType.IMMEDIATE: 0.8,      # High immediate impact
            InterventionType.ADAPTIVE: 0.6,       # Moderate sustained impact
            InterventionType.SUPPORTIVE: 0.4,     # Gradual improvement
            InterventionType.MOTIVATIONAL: 0.7,   # Good emotional boost
            InterventionType.COGNITIVE: 0.5       # Steady understanding improvement
        }
        
        predicted_improvement = improvement_factors.get(intervention_type, 0.5)
        
        return {
            'likelihood_of_success': f"{predicted_improvement * 100:.0f}%",
            'expected_timeframe': '5-15 minutes',
            'confidence_level': 'moderate' if predicted_improvement > 0.5 else 'low'
        }