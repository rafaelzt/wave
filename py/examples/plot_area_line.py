# Plot / Area + Line
# Make an area #plot with an additional line layer on top.
# ---
from h2o_wave import site, data, ui

page = site['/demo']

ice_cream_sales = [('2020-01-01', 650), ('2020-01-02', 600), ('2020-01-03', 450), ('2020-01-04', 530),
                   ('2020-01-05', 490), ('2020-01-06', 540), ('2020-01-07', 550), ('2020-01-08', 580),
                   ('2020-01-09', 570), ('2020-01-10', 610), ('2020-01-11', 630), ('2020-01-12', 680),
                   ('2020-01-13', 720), ('2020-01-14', 690), ('2020-01-15', 630), ('2020-01-16', 610)
                   ]

v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Area + Line - Ice Cream Sales',
    data=data('date sales', len(ice_cream_sales)),
    plot=ui.plot([ui.mark(type='area', x_scale='time', x='=date', y='=sales', y_min=300),
                  ui.mark(type='line', x='=date', y='=sales')
                  ])
))
v.data = ice_cream_sales

page.save()
