from django.shortcuts import render
# Create your views here.
from .models import Match, Player, Team

# Create your models here.


def index(request):
    context = {}
    matches = Match.objects.order_by('match_order')
    players = Player.objects.order_by('id')

    standings = []
    for p in players:
        one = Team.objects.raw("select id, sum(point) as points, sum(goal) as goal, sum(concede) as concede, sum(gd) as gd, \
                                sum(win) as win, sum(loss) as loss, sum(draw) as draw, sum(gd) as gd from wc_team \
                                where team_id = \'" + str(p.team_one_id) + "\'")
        two = Team.objects.raw("select id, sum(point) as points, sum(goal) as goal, sum(concede) as concede, sum(gd) as gd, \
                                sum(win) as win, sum(loss) as loss, sum(draw) as draw, sum(gd) as gd from wc_team \
                                where team_id = \'" + str(p.team_two_id) + "\'")
        three = Team.objects.raw("select id, sum(point) as points, sum(goal) as goal, sum(concede) as concede, sum(gd) as gd, \
                                sum(win) as win, sum(loss) as loss, sum(draw) as draw, sum(gd) as gd from wc_team \
                                where team_id = \'" + str(p.team_three_id) + "\'")
        four = Team.objects.raw("select id, sum(point) as points, sum(goal) as goal, sum(concede) as concede, sum(gd) as gd, \
                                sum(win) as win, sum(loss) as loss, sum(draw) as draw, sum(gd) as gd from wc_team \
                                where team_id = \'" + str(p.team_four_id) + "\'")

        total = int(one[0].points) + int(two[0].points) + int(three[0].points) + int(four[0].points)
        goals = int(one[0].goal if one[0].goal else 0) + int(two[0].goal if two[0].goal else 0) + int(three[0].goal if three[0].goal else 0) + \
            int(four[0].goal if four[0].goal else 0)
        gas = int(one[0].concede) + int(two[0].concede) + int(three[0].concede) + int(four[0].concede)
        gds = int(one[0].gd) + int(two[0].gd) + int(three[0].gd) + int(four[0].gd)
        win = int(one[0].win) + int(two[0].win) + int(three[0].win) + int(four[0].win)
        loss = int(one[0].loss) + int(two[0].loss) + int(three[0].loss) + int(four[0].loss)
        draw = int(one[0].draw) + int(two[0].draw) + int(three[0].draw) + int(four[0].draw)
        games = win + loss + draw

        standings.append({"name": p.player_name, "one": one[0].points, "two": two[0].points, "three": three[0].points, "four": four[0].points,
                          "win": win, "loss": loss, "draw": draw,
                          "goals": goals, "gas": gas, "gds": gds, "total": total, "games": games})

        sorted_standing = sorted(standings, key=lambda x: (x['total'], x['gds'], x['goals'], -x['gas']), reverse=True)

    context['matches'] = matches
    context['players'] = players
    context['standings'] = sorted_standing

    return render(request, 'index.html', context)
