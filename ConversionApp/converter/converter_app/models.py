from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return f'username: {self.username}, password: {self.password}'

class Quiz(models.Model):
    title = models.CharField(max_length=45)
    active = models.BooleanField(default=False)
    level = models.IntegerField()
    
    def __str__(self):
        return f'title: {self.title}, level: {self.level}'

class QuizQuestion(models.Model):
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    level = models.IntegerField()
    question = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question} : level {self.difficulty_level}"

class TakeQuiz(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    userQuizScore = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_id} took quiz {self.quizId} and scored {self.userQuizScore}"

class TakeQuestion(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    takeQuizId = models.ForeignKey(TakeQuiz, on_delete=models.CASCADE)
    questionId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    userAnswer = models.FloatField(default=None)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"User: {self.user_id} took question {self.questionId}, correct = {self.correct}"

class QuizQuestionAnswer(models.Model):
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quizQuestionId = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer = models.FloatField()
    
    def __str__(self):
        return f"Quiz: {self.quizId}, Quiz Question: {self.quizQuestionId}, answer: {self.answer} "

class ConversionFormulas(models.Model):
    formula_filepath = models.CharField(max_length=100)
    formula_name = models.CharField(max_length=100)
    
