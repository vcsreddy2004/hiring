from django.db import models
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = models.TextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True, null=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True, null=True)
    answer_hi = models.TextField(_("Answer (Hindi)"), blank=True, null=True)
    answer_bn = models.TextField(_("Answer (Bengali)"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        translator = Translator()
        try:
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, dest='hi').text
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, dest='bn').text
            if not self.answer_hi:
                self.answer_hi = translator.translate(self.answer, dest='hi').text
            if not self.answer_bn:
                self.answer_bn = translator.translate(self.answer, dest='bn').text
        except Exception as e:
            print(f"Translation failed: {e}")
        super().save(*args, **kwargs)

    def get_translation(self, lang):
        return {
            "question": getattr(self, f"question_{lang}", self.question),
            "answer": getattr(self, f"answer_{lang}", self.answer),
        }
    def __str__(self):
        return self.question
