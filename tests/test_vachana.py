# -*- coding: utf-8 -*-
"""
Unit tests for VachanaTTS integration
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from pythaitts import TTS


class TestVachanaIntegration(unittest.TestCase):
    """Test VachanaTTS integration"""

    @patch('pythaitts.pretrained.vachana_tts.VachanaTTS')
    def test_vachana_model_initialization(self, mock_vachana):
        """Test that VachanaTTS model can be initialized"""
        # Create TTS instance with vachana model
        tts = TTS(pretrained="vachana")
        
        # Verify model is loaded
        self.assertIsNotNone(tts.model)
        self.assertEqual(tts.pretrained, "vachana")

    @patch('pythaitts.pretrained.vachana_tts.VachanaTTS')
    def test_vachana_tts_call(self, mock_vachana_class):
        """Test calling tts method with vachana model"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.return_value = "/tmp/output.wav"
        mock_vachana_class.return_value = mock_instance
        
        # Create TTS instance
        tts = TTS(pretrained="vachana")
        
        # Call tts method
        result = tts.tts("สวัสดีครับ", speaker_idx="th_f_1", filename="/tmp/test.wav")
        
        # Verify the model was called with correct parameters
        mock_instance.assert_called_once()
        call_args = mock_instance.call_args
        self.assertEqual(call_args.kwargs['text'], "สวัสดีครับ")
        self.assertEqual(call_args.kwargs['speaker_idx'], "th_f_1")
        self.assertEqual(call_args.kwargs['filename'], "/tmp/test.wav")
        self.assertEqual(call_args.kwargs['return_type'], "file")

    @patch('pythaitts.pretrained.vachana_tts.VachanaTTS')
    def test_vachana_with_preprocessing(self, mock_vachana_class):
        """Test that preprocessing works with vachana model"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.return_value = "/tmp/output.wav"
        mock_vachana_class.return_value = mock_instance
        
        # Create TTS instance
        tts = TTS(pretrained="vachana")
        
        # Call tts method with text that needs preprocessing
        result = tts.tts("มี 5 คนๆ", speaker_idx="th_f_1", preprocess=True)
        
        # Verify preprocessing was applied
        mock_instance.assert_called_once()
        call_args = mock_instance.call_args
        processed_text = call_args.kwargs['text']
        
        # Text should have numbers converted and ๆ expanded
        self.assertNotIn("5", processed_text)
        self.assertNotIn("ๆ", processed_text)
        self.assertIn("ห้า", processed_text)
        self.assertIn("คนคน", processed_text)


if __name__ == '__main__':
    unittest.main()
