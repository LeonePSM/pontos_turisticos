def reprova_ponto(modeladmin, request, queryset):
    queryset.update(aprovado=False)


def aprova_ponto(modeladmin, request, queryset):
    queryset.update(aprovado=True)


reprova_ponto.short_description = 'Reprovar pontos'
aprova_ponto.short_description = 'Aprovar pontos'