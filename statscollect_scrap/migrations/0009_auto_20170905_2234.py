# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statscollect_scrap', '0008_processedgamesheetplayer_penalties_saved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footballratingscrapper',
            name='footballscrapper_ptr',
        ),
        migrations.RemoveField(
            model_name='footballratingscrapper',
            name='rating_source',
        ),
        migrations.RemoveField(
            model_name='footballscrapper',
            name='next_scrapper',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballgameresult',
            name='actual_away_team',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballgameresult',
            name='actual_home_team',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballgameresult',
            name='scrapped_step',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballstep',
            name='actual_instance',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballstep',
            name='actual_step',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballstep',
            name='actual_tournament',
        ),
        migrations.RemoveField(
            model_name='scrappedfootballstep',
            name='scrapper',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheet',
            name='actual_instance',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheet',
            name='actual_meeting',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheet',
            name='actual_step',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheet',
            name='actual_tournament',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheet',
            name='scrapper',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheetparticipant',
            name='actual_player',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheetparticipant',
            name='actual_team',
        ),
        migrations.RemoveField(
            model_name='scrappedgamesheetparticipant',
            name='scrapped_game_sheet',
        ),
        migrations.RemoveField(
            model_name='scrappedplayerratings',
            name='scrapped_meeting',
        ),
        migrations.RemoveField(
            model_name='scrappedplayerratings',
            name='teammeetingperson',
        ),
        migrations.RemoveField(
            model_name='scrappedplayerstats',
            name='teammeeting',
        ),
        migrations.RemoveField(
            model_name='scrappedplayerstats',
            name='teammeetingperson',
        ),
        migrations.RemoveField(
            model_name='scrappedteammeetingdata',
            name='scrapper',
        ),
        migrations.RemoveField(
            model_name='scrappedteammeetingdata',
            name='teammeeting',
        ),
        migrations.RemoveField(
            model_name='scrappedteammeetingratings',
            name='rating_source',
        ),
        migrations.RemoveField(
            model_name='scrappedteammeetingratings',
            name='scrapper',
        ),
        migrations.RemoveField(
            model_name='scrappedteammeetingratings',
            name='teammeeting',
        ),
        migrations.DeleteModel(
            name='FootballRatingScrapper',
        ),
        migrations.DeleteModel(
            name='FootballScrapper',
        ),
        migrations.DeleteModel(
            name='ScrappedFootballGameResult',
        ),
        migrations.DeleteModel(
            name='ScrappedFootballStep',
        ),
        migrations.DeleteModel(
            name='ScrappedGameSheet',
        ),
        migrations.DeleteModel(
            name='ScrappedGameSheetParticipant',
        ),
        migrations.DeleteModel(
            name='ScrappedPlayerRatings',
        ),
        migrations.DeleteModel(
            name='ScrappedPlayerStats',
        ),
        migrations.DeleteModel(
            name='ScrappedTeamMeetingData',
        ),
        migrations.DeleteModel(
            name='ScrappedTeamMeetingRatings',
        ),
    ]