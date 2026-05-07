# Tradonacci ICT Project Memory

Дата конспекта: 2026-05-06.

Источник: блог ICT Mentorship RUS на Teletype:
https://teletype.in/@tradonacci_ict

Назначение файла: рабочая память проекта по материалам Tradonacci ICT. Это не копия
статей, а сжатая спецификация правил, терминов и гипотез для разработки моделей,
фильтров и бэктестов в `ict_bot`.

## Как использовать

- Перед изменением ICT-моделей сначала читать этот файл, а не весь блог.
- К исходной статье возвращаться только если правило неоднозначно или нужен контекст.
- Не переносить правило в live без бэктеста против текущего baseline.
- Все FX-числа в пунктах адаптировать для crypto через ATR, bps или долю диапазона.
- В коде фиксировать, является ли правило HTF-контекстом, LTF-триггером, целью,
  stop/invalidation или post-filter.

## Scope

Изучено 48 опубликованных материалов блога плюс закрепленная дорожная карта:

- ICT Core Content: месяцы 1-4.
- ICT Forex Market Maker Series, 5 частей.
- ICT 2022 Mentorship summaries, episodes 2-3.
- Bridge Builder.
- Терминология, порядок изучения, Swing High/Swing Low.

Материалы по книгам и обучающему порядку сохранены только как источник контекста,
без влияния на торговые правила.

## Базовая терминология

- BSL: buyside liquidity, ликвидность выше максимумов.
- SSL: sellside liquidity, ликвидность ниже минимумов.
- EQH/EQL: равные максимумы/минимумы; почти всегда зона будущего снятия ликвидности.
- PDH/PDL: previous day high/low.
- HTF/LTF: старший/младший таймфрейм.
- MSB: market structure break.
- STH/STL: short-term high/low.
- ITH/ITL: intermediate-term high/low.
- LTH/LTL: long-term high/low.
- IDM: inducement.
- FVG: fair value gap.
- OB: order block.
- BB: breaker block.
- SMT: smart money technique, межрыночная/межсимвольная дивергенция.
- OTE: optimal trade entry, обычно зона 62%-79% коррекции.
- PD: premium/discount.
- BISI/SIBI: imbalance/inefficiency с направлением доставки цены.
- MMBM/MMSM: market maker buy/sell model.
- IOF: institutional order flow.
- DOL: draw on liquidity.
- POI: point of interest.
- CE: consequent encroachment, середина неэффективности/диапазона.
- PO3: power of three.
- KZ: killzone.

## Четыре состояния цены

Каждая торговая идея должна начинаться с определения текущего состояния рынка:

- Expansion: цена быстро уходит от equilibrium. Основной инструмент: OB.
- Retracement: цена возвращается в недавно созданный диапазон. Основные инструменты:
  FVG и liquidity void.
- Reversal: цена разворачивается после снятия ликвидности. Основной инструмент:
  liquidity pools / stop runs / turtle soup.
- Consolidation: цена стоит в четком диапазоне. Основной инструмент: equilibrium.

Практическое правило: сначала определить состояние, затем выбрать один инструмент.
Не смешивать все модели сразу. Одна хорошо протестированная модель достаточна.

## Top-down карта таймфреймов

Рекомендуемый объем истории для ручного и автоматического анализа:

- 1D: 9-12 месяцев.
- 4H: около 3 месяцев.
- 1H: около 3 недель.
- 15m: 3-4 дня.

Для бэктеста это означает, что warmup должен покрывать HTF-контекст, иначе модель
будет видеть setup без причины.

Разметка на каждом ТФ:

- быстрые смещения от уровня;
- недавние high/low без ретеста;
- чистые EQH/EQL;
- daily high/low;
- weekly high/low;
- session high/low;
- time of day / killzone формирования high/low.

## Time And Price

Время является первым фильтром, цена вторым.

Сессионные ориентиры из материалов:

- Asia range: примерно 20:00-00:00 NY.
- London: 02:00-05:00 NY.
- New York: 07:00-10:00 NY.
- Equity open reference: 09:30 NY.
- London close / reversal window: около 10:00 NY.
- День закрывается около 20:00 NY.

Типичный bullish day/week:

- Цена часто уходит ниже open перед основным ростом.
- Лучшие покупки возникают ниже или около daily/weekly open.
- Минимум bullish week часто формируется в понедельник, вторник или до NY-сессии среды.
- В четверг/пятницу вероятнее фиксация, возврат в weekly range или counter move.

Bearish week зеркальна:

- Предпочтительны продажи выше open в понедельник-среду.
- High недели часто формируется в первой половине недели.
- Четверг/пятница хуже для новых входов по направлению weekly bias.

FOMC / high-impact news:

- Может давать destroy model: снятие краткосрочных high и low до новости, затем
  сильная манипуляция и реальное движение.
- Для новых моделей такие дни лучше отмечать отдельным флагом, а не смешивать с
  обычными session setups.

## Bias And Draw On Liquidity

Главная задача HTF-анализа: определить, куда цена вероятнее стремится.

HTF draw может быть:

- liquidity pool;
- imbalance/FVG;
- liquidity void;
- old high/old low;
- OB или breaker на старшем ТФ.

Для сделки нужно заранее определить:

- текущий dealing range;
- premium/discount/equilibrium;
- internal range liquidity для входа;
- external range liquidity для выхода;
- низкое или высокое сопротивление до цели.

Входы ICT чаще используют internal liquidity: OB, FVG, liquidity void, CE,
equilibrium. Выходы чаще направлены на external liquidity: старые high/low,
EQH/EQL, PDH/PDL, session highs/lows.

## Premium, Discount, Equilibrium

Equilibrium: 50% текущего dealing range.

Для bullish bias:

- ниже equilibrium: discount, зона поиска покупок;
- глубокий discount: OTE примерно 62%-79%;
- цель часто в premium или на BSL.

Для bearish bias:

- выше equilibrium: premium, зона поиска продаж;
- цель часто в discount или на SSL.

Правило по invalidation:

- Если bullish идея уходит ниже исходного low диапазона, идея испорчена или требует
  нового turtle soup context.
- Если bearish идея уходит выше исходного high диапазона, идея испорчена или требует
  нового sweep context.

Материал подчеркивает: fair value в discount используется для покупок, fair value
в premium используется для продаж.

## Liquidity

Ликвидность находится там, где у участников стопы или пробойные ордера:

- выше swing high;
- выше EQH;
- выше high консолидации;
- ниже swing low;
- ниже EQL;
- ниже low консолидации;
- вокруг PDH/PDL и session high/low.

Swing High/Swing Low:

- swing high: три свечи, средняя имеет самый высокий high;
- swing low: три свечи, средняя имеет самый низкий low;
- цвет свечей не важен.

Важное различие:

- уровень с большим количеством price action вокруг него более защищен;
- движение через много старых swing points является high-resistance run;
- движение к ближайшей чистой ликвидности после сильного displacement является
  low-resistance run.

Для моделей нужно хранить:

- liquidity_side: BSL/SSL;
- liquidity_type: swing, equal_high_low, session, daily, weekly, range_boundary;
- clean_level: true/false;
- resistance_path: low/high/unknown;
- distance_to_liquidity_r или bps.

## Turtle Soup / Stop Run

Bullish turtle soup:

- HTF bias bullish или цена находится в discount/HTF POI.
- Цена нарушает старый low / EQL / SSL.
- Sell stops становятся рыночными продажами.
- Smart money покупает эту ликвидность.
- Требуется быстрая реакция вверх или LTF market structure shift.
- Цель: встречная BSL, FVG, OB, old high.

Bearish turtle soup зеркален:

- HTF bias bearish или цена в premium/HTF POI.
- Цена нарушает старый high / EQH / BSL.
- Buy stops становятся рыночными покупками.
- Smart money продает эту ликвидность.
- Требуется быстрая реакция вниз или LTF market structure shift.
- Цель: встречная SSL, FVG, OB, old low.

FX-ориентир из источника: если после sweep цена уходит слишком далеко против идеи,
это скорее continuation, а не reversal. Для crypto использовать ATR/bps threshold.

## False Breakouts Of Consolidation

В bullish условиях:

- Цена часто сначала выходит ниже консолидации за SSL.
- Затем возвращается внутрь диапазона и идет к BSL.
- Покупки ниже диапазона имеют больший смысл, чем покупка пробоя вверх.

В bearish условиях:

- Цена часто сначала выходит выше консолидации за BSL.
- Затем возвращается внутрь диапазона и идет к SSL.
- Продажи выше диапазона имеют больший смысл, чем продажа пробоя вниз.

Для кода:

- range_high / range_low;
- sweep_side;
- return_inside_range;
- target_opposite_range_side;
- trend_context.

## FVG And Liquidity Voids

FVG:

- Диапазон, где цена была доставлена односторонне.
- На HTF FVG часто на LTF виден как liquidity void.
- Цена может вернуться для rebalancing/redelivery.
- Возврат не обязан быть немедленным.

Liquidity void:

- Длинные односторонние свечи или gap-like движение.
- Цена часто возвращается покрыть void полностью или частично.
- После полного rebalancing не должно быть глубокого возврата через уровень,
  который подтвердил реакцию, если directional idea остается валидной.

Для моделей:

- gap_low/gap_high/ce;
- fill_depth: none/partial/ce/full/overfill;
- source_timeframe;
- time_to_fill_bars;
- displacement_before_gap;
- reaction_after_fill.

## Order Blocks

Bullish OB:

- Нисходящая свеча/бар перед сильным движением вверх.
- Лучше, если свеча находится рядом с support, discount, liquidity sweep или HTF POI.
- Подтверждение: последующая свеча нарушает high OB.
- Entry: возврат к телу OB, часто к high/open тела или CE/mean threshold.
- Risk: ниже тела OB или ниже wick, если используется полный диапазон.
- Лучшие OB обычно не торгуются глубже 50% тела после реакции.

Bearish OB зеркален:

- Восходящая свеча перед сильным движением вниз.
- Подтверждение: последующая свеча нарушает low OB.
- Entry: возврат к телу OB.
- Risk: выше тела или wick.

Несколько однонаправленных свечей подряд могут рассматриваться как один OB/block.

Фильтр качества:

- HTF bias должен поддерживать направление.
- Opposite-direction OB в сильном HTF trend чаще использовать как target или pause,
  а не как reversal entry.
- Immediate reaction от OB важна. Вялая реакция снижает качество.
- OB внутри internal range используется для entry, external liquidity для target.

Для кода:

- ob_body_low/high;
- ob_wick_low/high;
- ob_mean_threshold;
- confirmation_bars;
- retest_depth;
- immediate_reaction_bars;
- htf_alignment;
- inside_discount_or_premium.

## Mitigation Block

Bearish mitigation block:

- Цена идет к resistance/HTF POI.
- Формируется M-like sequence.
- Происходит bearish market structure shift ниже краткосрочного low.
- Покупатели внутри последнего ралли оказываются trapped.
- Возврат к их origin дает возможность mitigate loss.
- Smart money может использовать этот возврат для продаж.

Практическая зона:

- последняя down candle перед кратким ралли внутри trapped range;
- использовать весь диапазон свечи, включая wick;
- entry может быть у нижней части зоны;
- stop выше high этой свечи/зоны.

Bullish mitigation block зеркален.

Для кода:

- trapped_range_low/high;
- shift_break_level;
- mitigation_candle_range;
- retest_count;
- target_support_or_resistance.

## Breaker Block

Bullish breaker logic:

- Цена нарушает старый low и собирает SSL.
- Затем цена поднимается выше intervening short-term high.
- Это подтверждает bullish structure shift.
- Возврат к breaker zone рассматривается как long setup.
- Цель: resistance/BSL выше.

Bearish breaker logic:

- Цена нарушает старый high и собирает BSL.
- Затем цена падает ниже intervening short-term low.
- Это подтверждает bearish structure shift.
- Возврат к breaker zone рассматривается как short setup.
- Цель: support/SSL ниже.

Статья также описывает breaker через trapped participants: участники, открывшиеся
в сторону sweep, затем получают нарушение противоположной стороны и стремятся
mitigate loss на возврате.

Для кода:

- swept_level;
- intervening_swing;
- structure_shift_level;
- breaker_range;
- retest_window;
- retest_count;
- displacement_required.

## Rejection Block

Bearish rejection block:

- Сформирован high с длинными upper wicks.
- Цена торгуется выше тел свечей для снятия BSL, но не обязательно выше wick extreme.
- Важна зона между wick extreme и open/close тела.
- Возврат в эту зону может быть short trigger.

Bullish rejection block зеркален:

- Сформирован low с длинными lower wicks.
- Цена торгуется ниже тел свечей для снятия SSL.
- Важна зона между wick extreme и open/close тела.
- Возврат в эту зону может быть long trigger.

Практический вывод:

- Для liquidity sweep не всегда требуется high above wick или low below wick.
- Иногда достаточно нарушения тела/cluster bodies.
- Для take profit против позиции можно использовать open/close старых wick candles.

## Reclaimed Order Block

MMBM/MMSM контекст.

Bullish reclaimed OB:

- На sell curve smart money начинает аккумулировать позиции заранее.
- Небольшие bullish OB возникают перед краткими отскоками во время снижения.
- После достижения важной поддержки и смены направления эти старые OB могут быть
  reclaimed и работать как long zones на buy curve.

Bearish reclaimed OB зеркален:

- На buy curve smart money начинает распределять позиции заранее.
- Старые bearish OB затем используются как short zones на sell curve.

Для кода:

- source_ob_before_major_turn;
- curve_side: sell_curve/buy_curve;
- reclaimed_after_shift;
- support_or_resistance_reuse;
- sequence_position.

## Propulsion Block

Bullish propulsion block:

- Свеча торгуется внутрь предыдущего bullish OB / down candle.
- Затем принимает роль более чувствительной поддержки для движения вверх.
- Такой block не должен глубоко нарушать 50% тела.
- Часто retest high свечи дает быструю реакцию.

Bearish propulsion block зеркален.

Для кода:

- parent_ob;
- child_propulsion_candle;
- mean_threshold_hold;
- retest_to_high_or_low;
- immediate_reaction.

## Vacuum Block

Vacuum block:

- Gap/vacuum, созданный волатильным событием, open или news.
- Это реальная зона отсутствующей ликвидности.
- Не все gaps полностью закрываются.

Bullish context:

- Если внутри gap есть bullish OB, цена может заполнить gap частично и продолжить
  вверх, оставив часть vacuum open.
- Если time of day поддерживает full rebalance, цена может закрыть весь gap.
- После полного fill и bullish rally цена не должна снова глубоко провалиться под
  уровень, подтвердивший fill.

Временной фильтр:

- NY news/open чаще создает gap, который может быть заполнен.
- Late-day gap чаще может остаться открытым и стать будущим FVG.

Для кода:

- event_gap;
- session_created;
- partial_fill_allowed;
- full_fill_required;
- ob_inside_gap;
- gap_left_open.

## False Retail Patterns

Материалы явно трактуют популярные retail patterns как источники ликвидности,
а не как самостоятельные сигналы.

False flag:

- В HTF premium/near distribution bullish flag может быть trap.
- После fake upward continuation и downside break искать short на первом возврате
  к bearish OB.
- В HTF discount/near accumulation bearish flag может быть trap; применять зеркально.

False trendline:

- Диагональные линии субъективны.
- Очевидная линия поддержки/сопротивления создает ожидания retail.
- Третий touch или слишком очевидная линия часто является trap.
- Фокус должен быть на stops above/below swings и OB around trap.

Head and shoulders:

- Neckline break может быть не continuation, а liquidity sweep.
- В bullish environment classic H&S breakdown может быть long/turtle soup.
- Target для long может быть head/high.
- Inverse H&S зеркален.

Double top / double bottom:

- Не доверять как reversal pattern.
- Всегда ожидать снятие ликвидности за EQH/EQL.
- Measured move projection можно использовать как ориентир, насколько далеко за
  double top/bottom может пройти цена.
- Экстремумы диапазона имеют высокую вероятность, середина диапазона низкую.

False oscillator divergence:

- Индикаторная дивергенция не важнее ближайшей ликвидности.
- Если рядом есть obvious BSL/SSL, ожидать sweep, даже если oscillator показывает
  retail divergence.

## SMT Divergence

SMT используется между коррелированными или обратно коррелированными рынками.

FX/DXY:

- Если DXY делает lower low, FX-пара против USD должна часто делать higher high.
- Если DXY делает higher high, FX-пара против USD должна часто делать lower low.
- Симметрия подтверждает continuation.
- Несимметрия указывает на smart money participation и возможный reversal.

Ключевые сценарии:

- DXY lower low, FX не делает higher high: bullish DXY / bearish FX warning.
- DXY не делает higher high, FX делает lower low: bearish DXY / bullish FX warning.

Crypto adaptation:

- Использовать BTC/ETH/SOL как correlated pairs.
- Если один актив sweep high/low, а другой не подтверждает, это может быть SMT.
- Нужен отдельный backtest, потому что источник описывает в основном FX/DXY.

Для кода:

- reference_symbol;
- correlated_symbol;
- expected_symmetry;
- failed_swing_side;
- smt_direction;
- smt_strength;
- time_alignment_window.

## Institutional Sponsorship

Высококачественный setup должен иметь sponsorship:

- HTF displacement после sweep, discount/premium или fair value return.
- Ясный source level, откуда началось движение.
- Возврат к source OB/POI должен давать быструю реакцию.
- Вялая реакция означает отсутствие сильных институциональных ордеров.

Если реакция слабая:

- уменьшить риск;
- закрыть часть;
- отказаться от сделки;
- ждать continuation pattern вместо удержания плохой идеи.

Для кода:

- sponsorship_source_type;
- reaction_speed_bars;
- reaction_r_multiple;
- sluggish_reaction flag;
- reduce_risk_candidate flag.

## Risk And Trade Management

Основные правила из материалов:

- Стартовый риск: не более 1%-2%.
- Базовая цель: минимум 3R.
- Оптимальная модель: 1% risk и потенциал около 5R.
- Нельзя увеличивать риск после убытка.
- Если первая попытка выбита, но setup не сломан, повторный вход допустим с половиной
  первоначального риска.
- После повторного входа разумно зафиксировать прибыль около 2R, если она покрывает
  предыдущий убыток.

Для бэктеста:

- считать expectancy не только win rate;
- отдельно считать managed expectancy;
- моделировать partial close / BE;
- хранить first_attempt_loss и reentry_allowed как отдельную гипотезу, не смешивать
  с базовым setup.

## High Reward Setup Checklist

Сильный setup требует согласования перспектив.

Broad perspective: желательно минимум 2 фактора:

- macro;
- interest rates;
- intermarket analysis;
- seasonality.

Intermediate perspective: желательно минимум 2 фактора:

- top-down HTF analysis;
- COT;
- market sentiment.

Short-term perspective: желательно все 3:

- correlation / SMT;
- time and price;
- IPDA / liquidity / IOF.

Для crypto сейчас broad/intermediate факторы могут быть ограничены. Поэтому нельзя
притворяться, что macro/COT есть в модели, если данных нет. Лучше добавить
`macro_context=unknown` и не использовать это как gate.

## Model-Specific Backtest Hypotheses

Turtle Soup:

- Усилить качество через HTF discount/premium, clean EQH/EQL, session timing,
  SMT, immediate reaction и low-resistance path.
- Отдельно тестировать sweep body-only vs wick-extreme.
- Отдельно тестировать max sweep depth через ATR/bps.

Silver Bullet:

- Усилить через killzone, FVG creation, return to FVG/CE, DOL to opposing liquidity.
- Не смешивать с random FVG outside time window.

IFVG/FVG Retest:

- Различать HTF FVG, LTF liquidity void и full/partial fill.
- Добавить time_to_retest_bars, fill_depth, reaction_after_fill.

Breaker Block:

- Требовать sweep + structure shift + retest.
- Ограничить retest_count.
- Проверить displacement_required.

Reclaimed OB:

- Моделировать последовательность MMBM/MMSM: old OBs formed before major support/resistance,
  then reused after curve shift.
- Нужен sequence_position, иначе модель будет ловить обычные OB.

Rejection Block:

- Тестировать body-liquidity sweep без обязательного wick break.
- Использовать wick-to-body range как POI.

Mitigation Block:

- Требовать trapped participants + shift.
- Тестировать full candle range vs body-only range.

Propulsion/Vacuum Blocks:

- Пока не включать в live без отдельного baseline.
- Полезны как research-only models или quality tags для OB/FVG.

## Data Fields Worth Adding Or Preserving

- htf_bias
- htf_objective_type
- htf_draw_direction
- htf_location
- htf_zone_type
- dealing_range_low/high/source
- equilibrium
- premium_discount_location
- liquidity_side
- liquidity_type
- clean_liquidity
- body_liquidity
- wick_liquidity
- sweep_depth_bps
- sweep_depth_atr
- return_inside_range
- structure_shift_level
- displacement_grade
- displacement_factor
- fvg_low/high/ce
- fvg_fill_depth
- liquidity_void_low/high
- ob_body_low/high
- ob_wick_low/high
- ob_mean_threshold
- ob_retest_depth
- immediate_reaction_bars
- session_window
- ny_time
- smt_pair
- smt_direction
- smt_strength
- low_resistance_path
- target_external_liquidity
- invalidation_source
- no_trade_reasons

## NotebookLM ICT Operational Rules

Дата добавления: 2026-05-06.

Эти правила имеют приоритет для алгоритмизации текущих intraday-моделей на crypto. Если они конфликтуют со
старым исследовательским baseline, сначала менять спецификацию модели, затем заново прогонять backtest.

Intraday sessions, NY time:

- London Open: 02:00-05:00 NY, допускается как SHOULD-фильтр.
- NY Open / Morning: 07:00-10:00 NY, основной MUST-контекст.
- NY PM Session: 13:30-16:00 NY, допускается как SHOULD-контекст.
- Silver Bullet AM: 10:00-11:00 NY, MUST.
- Silver Bullet PM: 14:00-15:00 NY, MUST.
- NY Lunch: 12:00-13:00 NY, SHOULD no-trade.
- После 16:00 NY до Asia open: MUST no-trade для intraday-моделей.

Daily / HTF bias:

- Торговый bias строится на Daily/4H, глобальный контекст на Weekly/Monthly.
- Bullish: HTF HH/HL, bullish PD arrays удерживаются, bearish PD arrays пробиваются.
- Bearish: HTF LH/LL, bearish PD arrays удерживаются, bullish PD arrays пробиваются.
- Long разрешен только в discount текущего dealing range; short только в premium.
- DOL должен учитывать PDH/PDL, EQH/EQL и старые high/low как основные цели.
- Bias недействителен после достижения HTF target или подтвержденного BOS против bias.

Silver Bullet:

- Валидный setup: новый FVG или первый тест существующего FVG строго внутри 10:00-11:00 или 14:00-15:00 NY.
- FVG может быть создан до окна, если entry/retest происходит внутри окна; лучший случай - создание и тест внутри окна.
- Entry: edge FVG или CE 50%.
- Retest wait: не более 15-20 LTF баров на 1m/5m; для 15m это должно быть ужато отдельным backtest-фильтром.
- Stop: за ближайший local swing high/low или за MT ближайшего Order Block.
- Target: минимум 2R или ближайшая session liquidity.
- HTF draw on liquidity обязателен; SMT optional.

Turtle Soup / Stop Run:

- Обязателен wick sweep значимого уровня: PDH/PDL, EQH/EQL, old high/low.
- Обязательны rejection и закрытие обратно внутри диапазона.
- MSS или FVG на младшем TF делает setup A+.
- Для crypto-adapted версии SMT BTC/ETH на sweep обязателен.
- Между sweep и confirmation желательно не более 3-5 баров.
- Entry: retest пробитого экстремума или market после close-back.
- Invalidation: body close за sweep extreme, потому что sweep превращается в BOS.

ICT 2022 model:

- Последовательность MUST: HTF POI test -> liquidity sweep -> MSS -> displacement/FVG -> retest.
- Sweep и MSS желательно внутри одной session; retest может быть позже, но только до достижения target.
- Displacement candle обязана иметь body/range > 70%.
- Entry: edge или CE созданного FVG.
- Stop: за sweep extreme.
- Target: противоположная external liquidity, BSL/SSL.

Trade management:

- Риск фиксируется как процент депозита на stop.
- TP1: первый проблемный уровень или 1R.
- После TP1 или сильного impulse допускается BE.
- Partials: 25-50% позиции на TP1 optional.
- Final target: old highs/lows, BSL/SSL или HTF PD arrays.
- Setup отменяется, если target достигнут до возврата в entry zone.

Quality metadata:

- session_type
- bias_alignment
- is_in_p_d
- smt_detected
- displacement_grade / body_range_ratio
- fvg_fill_depth
- time_to_target
- invalidated_at

## Source Index

Pinned roadmap:

- Привет: https://teletype.in/@tradonacci_ict/5LwbY6JsBS8

Core Content Month 1:

- Элементы торгового сетапа: https://teletype.in/@tradonacci_ict/8fqO6P0Oe8x
- Как маркет-мейкеры обусловливают рынок: https://teletype.in/@tradonacci_ict/NfgH_Va9SS4
- На чем фокусироваться прямо сейчас: https://teletype.in/@tradonacci_ict/p6z1ilyPRZ6
- Equilibrium Vs. Discount: https://teletype.in/@tradonacci_ict/_Yhr0OlheeF
- Equilibrium Vs. Premium: https://teletype.in/@tradonacci_ict/aj3lFISf8aa
- Справедливая стоимость: https://teletype.in/@tradonacci_ict/1iGC-BkOqF8
- Ликвидность: https://teletype.in/@tradonacci_ict/Zb7OzbfFAe1
- Импульсные колебания цен и замедление рынка: https://teletype.in/@tradonacci_ict/fLdNi3iztSK

Core Content Month 2:

- Небольшие аккаунты без высокого риска: https://teletype.in/@tradonacci_ict/JECqSZie36S
- Сетапы с низким риском: https://teletype.in/@tradonacci_ict/j3FoMIQxWme
- Нет страха потерять деньги: https://teletype.in/@tradonacci_ict/9cizMrja-CD
- Смягчить убыточные сделки: https://teletype.in/@tradonacci_ict/_6tYZjjacsE
- Сетапы с высоким вознаграждением: https://teletype.in/@tradonacci_ict/_Y9be999BWf
- Ложный флаг: https://teletype.in/@tradonacci_ict/o-WBIcnqcXA
- Ложные пробои: https://teletype.in/@tradonacci_ict/6xKVEyzxshd

Core Content Month 3:

- Выбор таймфрейма и модели: https://teletype.in/@tradonacci_ict/5XAQ_a1ER_8
- Институциональный поток заказов: https://teletype.in/@tradonacci_ict/jVuwN7jIOKi
- Институциональное спонсорство: https://teletype.in/@tradonacci_ict/VLQdVjvcbjd
- SMT дивергенция: https://teletype.in/@tradonacci_ict/nKjU4AEmE8f
- Macro to micro Forex: https://teletype.in/@tradonacci_ict/jZOMz52b8V4
- Ложные линии тренда: https://teletype.in/@tradonacci_ict/S0IRoYcyFty
- Голова-плечи trap: https://teletype.in/@tradonacci_ict/DdejzvWbMmz

Core Content Month 4:

- Процентные ставки и валюты: https://teletype.in/@tradonacci_ict/Jy6tOavhoQy
- Ликвидность и доставка цены: https://teletype.in/@tradonacci_ict/sSwE03wLigl
- Order Blocks: https://teletype.in/@tradonacci_ict/jLa0yQhACsO
- Mitigation Blocks: https://teletype.in/@tradonacci_ict/OCy27V4UjJ2
- Breaker Block: https://teletype.in/@tradonacci_ict/UohD0NHEjKW
- Rejection Block: https://teletype.in/@tradonacci_ict/jlxv0lGgTwq
- Reclaimed Orderblock: https://teletype.in/@tradonacci_ict/Sm4FYlo2raK
- Propulsion Block: https://teletype.in/@tradonacci_ict/-sGoiz0KCBR
- Vacuum Block: https://teletype.in/@tradonacci_ict/xLM6VzkCg31
- Liquidity Voids: https://teletype.in/@tradonacci_ict/1F_iLhWXchd
- Liquidity Pools: https://teletype.in/@tradonacci_ict/lreIKU0KNoJ
- FVG: https://teletype.in/@tradonacci_ict/zRhtf83KyM9
- Ложная дивергенция: https://teletype.in/@tradonacci_ict/bVojCifj6nb
- Double top / double bottom: https://teletype.in/@tradonacci_ict/K2VV1PZV36y

Market Maker Series:

- Vol. 1 Macro: https://teletype.in/@tradonacci_ict/7uZMINUZ42l
- Vol. 2 IOF and liquidity: https://teletype.in/@tradonacci_ict/Yg20Trr17mK
- Vol. 3 Structure, key levels, SMT: https://teletype.in/@tradonacci_ict/-b1_PalXJC1
- Vol. 4 Time and price: https://teletype.in/@tradonacci_ict/tND309-YuXJ
- Vol. 5 Daily bias/macros: https://teletype.in/@tradonacci_ict/IlQgSVZwors

Other:

- Bridge Builder: https://teletype.in/@tradonacci_ict/TLDz0iGYtd5
- 2022 Mentorship Episode 2 Summary: https://teletype.in/@tradonacci_ict/vm_-8GXrd8G
- 2022 Mentorship Episode 3 Summary: https://teletype.in/@tradonacci_ict/Ez7o05Qh_YS
- Терминология: https://teletype.in/@tradonacci_ict/7n2gjgR0sTt
- Swing High/Swing Low: https://teletype.in/@tradonacci_ict/naSAWfRBQ7a
- Порядок изучения: https://teletype.in/@tradonacci_ict/YYdfUb5qa6S
- Книги: https://teletype.in/@tradonacci_ict/yQbcU5FL8H1
