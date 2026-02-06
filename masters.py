import marimo

__generated_with = "0.19.7"
app = marimo.App(width="columns", auto_download=["html"])

with app.setup:
    import marimo as mo
    import pandas as pd
    import altair as alt

    from textwrap import wrap

    @alt.theme.register('serif', enable=True)
    def serif() -> alt.theme.ThemeConfig:
        return {
            "autosize": {"contains": "content", "resize": True},
            "config": {
                "font": "Times New Roman",
                "axisX": {"labelFontSize": 7}
            },
            "height": 200,
            "width": 600
        }


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Genders
    """)
    return


@app.cell
def _(responses):
    _chart = (
        alt.Chart(responses)
        .encode(
            color=alt.Color(field='Gender', type='nominal', sort=['Male', 'Female', 'Nonbinary', 'Genderfluid', 'Other']),
            theta=alt.Theta(aggregate='count', type='quantitative').stack(True),
        )
        .properties(width='container')
    )
    _pie = _chart.mark_arc(outerRadius=100)
    _text = _chart.mark_text(radius=110).encode(text='count(Gender):Q')
    _chart = _pie + _text
    _chart.save('genders.pdf')
    _chart
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Employment
    """)
    return


@app.cell
def _(employment_status):
    _chart = (
        alt.Chart(employment_status)
        .encode(
            y=alt.Y('Status:N', sort=["Employed", "Student", "Researcher", "None of the above"]),
            x=alt.X('Count:Q').stack(True),
        )
        .properties(width='container')
    )
    _chart = _chart.mark_bar() + _chart.mark_text(align="left", dx=2).encode(text='Count:Q')
    _chart.save('employment.pdf')
    _chart
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Ages
    """)
    return


@app.cell
def _(responses):
    # Ages
    _chart = (
        alt.Chart(responses)
        .mark_bar()
        .encode(
            x=alt.X(field='Age (Years)', type='quantitative', sort='ascending'),
            y=alt.Y(aggregate='count', type='quantitative'),
            tooltip=[
                alt.Tooltip(field='Age (Years)', format=',.0f'),
                alt.Tooltip(aggregate='count')
            ]
        )
    )
    _chart.save("ages.pdf")
    _chart
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Scenarios
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Counts
    """)
    return


@app.cell
def _(s1, s2, s3, s4, s5):
    _charts = []
    for _i, _scenario, in enumerate([s1, s2, s3, s4, s5]):
        _chart = alt.Chart(_scenario).mark_bar().encode(
            x=alt.X("Question", sort=None).axis(
                titleAngle=0,
                labelAngle=0
            ),
            xOffset="Value:N",
            y=alt.Y("Count:Q"),
            color=alt.Color("Value:N")
        )
        _chart.save(f'scenario{_i+1}.pdf')
        _charts.append(_chart)
    _charts
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Averages
    """)
    return


@app.cell
def _(s1_avg, s2_avg, s3_avg, s4_avg, s5_avg):
    _charts = []
    for _i, _scenario, in enumerate([s1_avg, s2_avg, s3_avg, s4_avg, s5_avg]):
        _chart = alt.Chart(_scenario.reset_index()).mark_bar().encode(
            x=alt.X("Question", sort=None).axis(
                titleAngle=0,
                labelAngle=0
            ),
            y=alt.Y(
                "Average:Q",
                scale=alt.Scale(domain=[0, 5])
            ),
        )
        _chart.save(f'scenario{_i+1}_averages.pdf')
        _charts.append(_chart)
    _charts
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Differences
    """)
    return


@app.cell
def _(s1to2, s1to3, s1to4, s1to5, s2to3, s2to4, s2to5, s3to4, s3to5, s4to5):
    _charts = []
    _names = [
        "1 to 2",
        "1 to 3",
        "1 to 4",
        "1 to 5",
        "2 to 3",
        "2 to 4",
        "2 to 5",
        "3 to 4",
        "3 to 5",
        "4 to 5",
    ]
    for _i, _scenario, in enumerate([s1to2, s1to3, s1to4, s1to5, s2to3, s2to4, s2to5, s3to4, s3to5, s4to5]):
        _chart = alt.Chart(_scenario.reset_index(), title=f'Difference from Scenario {_names[_i]}').mark_bar().encode(
            x=alt.X(
                "Question", 
                sort=None,
            ).axis(
                titleAngle=0,
                labelAngle=0
            ),
            y=alt.Y(
                "Average:Q",
                scale=alt.Scale(domain=[-2.5, 2.5])
            )
        )
        _chart.save(f'scenario{_names[_i]}_change.pdf')
        _charts.append(_chart)
    _charts
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Sentiments
    """)
    return


@app.cell
def _(responses):
    _chart = (
        alt.Chart(responses)
        .mark_bar()
        .encode(
            x=alt.X(field='What is your current opinion of generative artificial intelligence tools?', type='nominal'),
            y=alt.Y(aggregate='count', type='quantitative'),
        )
        .properties(
            width=300,
        )
    )
    _chart.save('self-sentiments.pdf')
    _chart
    return


@app.cell
def _(responses):
    _labels = {
        '❌': "Negative", 
        '⚠️': "Mixed", 
        '✅': "Positive", 
        '': "No free text comment"
    }
    _charts = []
    for _sentiment in ['❌', '⚠️', '✅', '']:
        _data = responses[responses["Sentiments.Sentiment"] == _sentiment]
        _data = _data['What is your current opinion of generative artificial intelligence tools?'].value_counts()
        for _i in range(1, 6):
            if (_i not in _data):
                _data[_i] = 0

        _chart = (
            alt.Chart(_data.reset_index())
            .mark_bar()
            .encode(
                x=alt.X('What is your current opinion of generative artificial intelligence tools?:N'),
                y=alt.Y('count:Q'),
            )
            .properties(
                width=300,
            )
        )
        _chart.save(f'self-sentiments{_labels[_sentiment]}.pdf')
        _charts.append(_chart)
    _charts
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Sentiment coding
    """)
    return


@app.cell
def _(all_sentiments):
    _chart = (
        alt.Chart(all_sentiments)
        .mark_arc(innerRadius=0)
        .encode(
            color=alt.Color('Sentiment:N', sort=['Positive', 'Negative', 'Mixed', 'N/A']),
            theta=alt.Theta('Percentage:Q', stack="normalize")
        )
        .properties(
            width='container',
        )
    )
    _chart = _chart.mark_arc(outerRadius=100) + \
             _chart.mark_text(
                 radius=60,
                 align="right"
             ).encode(
                 text=alt.Text('Percentage:Q', format=".1%"),
                 color=alt.value("white"),
             )
    _chart.save('sentiments_coded.pdf')
    _chart
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Groups
    """)
    return


@app.cell
def _(
    Region_EMEA,
    Region_NA,
    employed,
    imagevideo,
    noimagevideo,
    older,
    ooee,
    researcher,
    responses,
    sentiment_mixed,
    sentiment_negative,
    student,
    younger,
):
    _groups = [
        ('All', responses),
        ('Older', older),
        ('Younger', younger),
        ('Region NA', Region_NA),
        ('Region EMEA', Region_EMEA),
        ('Image/Video', imagevideo),
        ('No Image/Video', noimagevideo),
        ('Employed', employed),
        ('Student', student),
        ('Researcher', researcher),
        ('OOEE', ooee),
        ('Sentiment negative', sentiment_negative),
        ('Sentiment mixed', sentiment_mixed),
    ]

    _opinions = []

    for _i, (_groupname, _group) in enumerate(_groups):
        _mean = _group['What is your current opinion of generative artificial intelligence tools?'].mean()
        _opinions.append({
            'Group': _groupname,
            'Mean opinion': _mean,
            'Count': len(_group),
            "i": _mean
        })
        print(_groupname, len(_group))

    _opinions = pd.DataFrame(_opinions)

    _chart = (
        alt.Chart(_opinions)
        .mark_tick()
        .encode(
            x=alt.X('Mean opinion:Q').scale(zero=False, domain=[1, 2.5]),
            color=alt.Color('Group:N')
        )
    )
    _text = _chart.mark_text(
        align='center',
        baseline='top',
    ).encode(
        text='Group',
        y=alt.Y('i:N').axis(labels=False, title=None)
    )
    _chart = (_chart + _text).configure_tick(thickness=2).resolve_scale(y ='independent')
    _chart.save('sentiment_group_means.pdf')

    (_chart, _opinions)
    return


@app.cell
def _(responses):
    _splits = []

    for _i in range(responses["Age (Years)"].min(), responses["Age (Years)"].max() - 1):
        _older = responses[responses['Age (Years)'] > _i]
        _younger = responses[responses['Age (Years)'] <= _i]
        _splits.append({
            "Split point": _i,
            "Group": 'Older than',
            "n": len(_older),
            "Mean": _older['What is your current opinion of generative artificial intelligence tools?'].mean(),
        })
        _splits.append({
            "Split point": _i,
            "Group": 'Younger than',
            "n": len(_younger),
            "Mean": _younger['What is your current opinion of generative artificial intelligence tools?'].mean()
        })

    _splits = pd.DataFrame(_splits)

    _chart = (
        alt.Chart(_splits)
        .mark_line()
        .encode(
            x=alt.X("Split point:Q"),
            y=alt.Y("Mean:Q").scale(zero=False),
            color=alt.Color("Group:N")
        )
    )

    _line = _chart.mark_area().encode(
        alt.Y('n:Q'),
        color=alt.Color('Group:N'),
        fillOpacity=alt.OpacityValue(0.35)
    )

    _chart = alt.layer(_line, _chart).resolve_scale(y='independent', color='independent')

    _chart.save('age_sentiment_depending_on_split.pdf')

    (_chart, _splits)
    return


@app.cell(column=1)
def _():
    # All responses 
    responses = pd.read_excel('responses.xlsx', sheet_name="Raw Responses")
    responses = responses.fillna('')
    return (responses,)


@app.cell
def _(responses):
    responses
    return


@app.cell
def _(responses):
    # Employment
    employed = responses[responses['Select any or all groups that apply to you']
        .str.contains('Employed', na=False)]
    student = responses[responses['Select any or all groups that apply to you']
        .str.contains('Student', na=False)]
    researcher = responses[responses['Select any or all groups that apply to you']
        .str.contains('Researcher', na=False)]
    ooee = responses[~responses['Select any or all groups that apply to you']
        .str.contains('Student|Employed|Researcher', na=False)]

    # Regions
    Region_NA = responses[responses['Region'] == "North America"]
    Region_EMEA = responses[responses['Region'] == "EMEA"]

    imagevideo = responses[responses["Which methods have you used to interact with generative AI?"]
        .str.contains('Image/Video', na=False)]
    noimagevideo = responses[~responses["Which methods have you used to interact with generative AI?"]
        .str.contains('Image/Video', na=False)]

    sentiment_negative = responses[responses["Sentiments.Sentiment"] == "❌"]
    sentiment_mixed = responses[responses["Sentiments.Sentiment"] == "⚠️"]
    return (
        Region_EMEA,
        Region_NA,
        employed,
        imagevideo,
        noimagevideo,
        ooee,
        researcher,
        sentiment_mixed,
        sentiment_negative,
        student,
    )


@app.cell
def _(responses):
    age_split = mo.ui.slider.from_series(responses["Age (Years)"], value=31)
    age_split
    return (age_split,)


@app.cell
def _(age_split, responses):
    # Ages
    older = responses[responses['Age (Years)'] > age_split.value]
    younger = responses[responses['Age (Years)'] <= age_split.value]
    return older, younger


@app.cell
def _(employed, ooee, researcher, student):
    employment_status = pd.DataFrame([
        ("Employed", len(employed)),
        ("Student", len(student)),
        ("Researcher", len(researcher)),
        ("None of the above", len(ooee))
    ], columns=['Status', 'Count'])
    return (employment_status,)


@app.cell
def _():
    # Scenarios

    question_labels = [
        'This system is an example of generative AI',
        'I did the majority of the work',
        'I played a key part in the creation of the output',
        'The output represents my creative vision',
        'I would describe the output as my own',
        'I was in control of the output',
        'I know about a real service or feature like this',
        'I have used a service or feature like this'
    ]
    short_labels = [
        'Is GenAI',
        'Majority my work',
        'I played a key part',
        'Represents my vision',
        'Would describe as mine',
        'I was in control',
        'Know of this tool',
        'Have used this tool'
    ]
    return question_labels, short_labels


@app.cell
def _(question_labels, responses, short_labels):
    scenarios = {}
    for _i in range(1, 6):
        scenarios[_i] = {}
        for _j, _question in enumerate(question_labels):
            _key = f'Scenario {_i} [{_question}]'
            scenarios[_i][short_labels[_j]] = responses[_key]

    scenario_counts = []
    for _scenario, _questions in scenarios.items():
        for _question, _answers in _questions.items():
            _values = _answers.value_counts()
            for _v in range(1, 6):
                if _v in _values:
                    _count = _values[_v]
                else:
                    _count = 0
                scenario_counts.append({
                    'Scenario': _scenario, 
                    'Question': _question, 
                    'Value': _v, 
                    'Count': _count}
                )
    scenario_counts = pd.DataFrame(scenario_counts)

    # Averages
    scenario_averages = []
    for _scenario, _questions in scenarios.items():
        for _question, _answers in _questions.items():
            scenario_averages.append({
                'Scenario': _scenario,
                'Question': _question,
                "Average": _answers.mean()
            })
    scenario_averages = pd.DataFrame(scenario_averages).set_index('Question')
    return scenario_averages, scenario_counts


@app.cell
def _(scenario_counts):
    s1, s2, s3, s4, s5 = [scenario_counts[scenario_counts['Scenario'] == x] for x in range(1, 6)]
    return s1, s2, s3, s4, s5


@app.cell
def _(scenario_averages):
    s1_avg, s2_avg, s3_avg, s4_avg, s5_avg = [scenario_averages[scenario_averages['Scenario'] == x] for x in range(1, 6)]
    return s1_avg, s2_avg, s3_avg, s4_avg, s5_avg


@app.cell
def _(s1_avg, s2_avg, s3_avg, s4_avg, s5_avg):
    s1to2, s1to3, s1to4, s1to5, s2to3, s2to4, s2to5, s3to4, s3to5, s4to5 = [s1_avg.copy() for x in range(10)]

    s1to2['Average'] = s2_avg['Average'] - s1_avg['Average']
    s1to3['Average'] = s3_avg['Average'] - s1_avg['Average']
    s1to4['Average'] = s4_avg['Average'] - s1_avg['Average']
    s1to5['Average'] = s5_avg['Average'] - s1_avg['Average']
    s2to3['Average'] = s3_avg['Average'] - s2_avg['Average']
    s2to4['Average'] = s4_avg['Average'] - s2_avg['Average']
    s2to5['Average'] = s5_avg['Average'] - s2_avg['Average']
    s3to4['Average'] = s4_avg['Average'] - s3_avg['Average']
    s3to5['Average'] = s5_avg['Average'] - s3_avg['Average']
    s4to5['Average'] = s5_avg['Average'] - s4_avg['Average']
    return s1to2, s1to3, s1to4, s1to5, s2to3, s2to4, s2to5, s3to4, s3to5, s4to5


@app.cell
def _(Region_EMEA, Region_NA, employed, ooee, responses, student):
    all_sentiments = percentageSentiments(responses)

    sentiments_NA = percentageSentiments(Region_NA)
    sentiments_EMEA = percentageSentiments(Region_EMEA)

    sentiments_student = percentageSentiments(student)
    sentiments_employed = percentageSentiments(employed)
    sentiments_ooee = percentageSentiments(ooee)
    return (all_sentiments,)


@app.function
def percentageSentiments(frame):
    _frame = frame['Sentiments.Sentiment'].value_counts()
    _frame = [
        ("Negative", round(_frame['❌'] / _frame.sum(), 3)),
        ("Mixed", round(_frame['⚠️'] / _frame.sum(), 3)),
        ("Positive", round(_frame['✅'] / _frame.sum(), 3)),
        ("N/A", round(_frame[''] / _frame.sum(), 3))
    ]
    return pd.DataFrame(_frame, columns=["Sentiment", "Percentage"])


@app.cell
def _(responses):
    (
        responses['Sentiments.Sentiment'].value_counts(),
        len(responses[responses['Sentiments.Sentiment'] != ''])
    )
    return


@app.cell
def _(responses):
    _columns = [
        ('Sentiments.Bad Output', 'Bad Output'),
        ('Sentiments.Theft',  'Theft'),
        ('Sentiments.Environment', 'Environment'),
        ('Sentiments.Human replacement', 'Human Replacement'),
        ('Sentiments.Economy', 'Economy'),
        ('Sentiments.Sycophancy Mental harm', 'Sycophancy or Other Mental Harm'),
        ('Sentiments.Disinfo', 'Disinformation'),
        ('Sentiments.Other Ethics', 'Other Ethical Concern'),
        ('Sentiments.Forced on you', 'Forced On You'),
        ('Sentiments.Oversold', 'Oversold'),
        ('Sentiments.Toy', 'Toy'),
        ('Sentiments."Outweigh" / Net Negative', 'Net Negative'),
        ('Sentiments.Negative view of owners', 'Negative View Of Owners'),
        ('Sentiments.Negative image of users', 'Negative View Of Users'),
        ('Sentiments.General concerns', 'General Concerns'),
        ('Sentiments.Valid formal uses', 'Recognize Valid Formal Uses'),
        ('Sentiments.Slop hose', '"Slop Hose"'),
        ('Sentiments.Regulation', 'Need For Regulation'),
    ]

    print(len(_columns))
    for _column, _column_label in _columns:
        print(_column_label, len(responses[responses[_column] == '✅']))
    return


if __name__ == "__main__":
    app.run()
