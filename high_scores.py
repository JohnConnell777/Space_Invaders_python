from intro import Title


class HighScoreScreen:
    def __init__(self, ai_settings, screen, game_stats):
        self.score_text = []
        self.score_text.append(Title(ai_settings.bg_color, screen, 'High Scores'))
        for num, value in enumerate(game_stats.high_scores_all, 1):
            self.score_text.append(Title(ai_settings.bg_color, screen, str(num) + '.   ' + str(value),
                                         text_color=(0, 255, 0)))

        y_offset = ai_settings.screen_height * 0.15
        for text in self.score_text:
            text.prep_image()
            text.image_rect.centerx = ai_settings.screen_width // 2
            text.image_rect.centery = y_offset
            y_offset += ai_settings.screen_height * 0.15

    def show_scores(self):
        for text in self.score_text:
            text.blitme()
