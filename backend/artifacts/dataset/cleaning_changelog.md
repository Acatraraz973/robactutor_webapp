# RoBacTutor Dataset Cleaning Changelog

Input: `robactutor_sft_dataset_reviewed.jsonl` (157 records)
Output: `robactutor_sft_dataset_cleaned.jsonl`

## Citation removal

157 of 157 records (100.0%) contained the fabricated "baremul oficial ANCE <year>" citation; it was stripped in each.

- istorie: 26
- limba_engleza: 34
- limba_romana: 73
- matematica: 24

## Duplication candidates -- MANUAL REVIEW REQUIRED

136 records flagged as possible duplicated/spliced text (NOT auto-fixed -- see dataset_quality_audit.py notes on why this can't be done reliably). Read each and decide:

### Record 3 (istorie) -- match ratio 1.00
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 4: C..."

Span A: `1p. x2 – menționează două`

Span B: `1p. x2 – menționează două`

Full response: **Răspuns și explicație (1 puncte):**

Amplasarea în timp și spațiu a Amplasarea în timp (2 p) evenimentelor/proceselor/ 1p. x2 – menționează două date cronologice fenomenelor istorice. relevante. 4 puncte Amplasarea în spațiu (2) 1p. x2 – menționează două țări/ regiuni/ continente/ părți ale lumii....

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 8 (istorie) -- match ratio 1.00
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 4: E..."

Span A: `1p. x2 – menționează două`

Span B: `1p. x2 – menționează două`

Full response: **Răspuns și explicație (1 puncte):**

Amplasarea în timp și spațiu a Amplasarea în timp (2 p) evenimentelor/proceselor/ 1p. x2 – menționează două date cronologice fenomenelor istorice. relevante. 4 puncte Amplasarea în spațiu (2) 1p. x2 – menționează două țări/ regiuni/ continente/ părți ale lumii....

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 15 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: According to the text, Brazilian art..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 16 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 4: According to the text, French artist..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (4 puncte):**

Corectitudinea la nivel de competenţă lingvistică (componenta gramaticală şi ortografică) - 4 puncte. Utilizează, ortografiază corect modurile, timpurile, formele şi 0 1 2 3 4 structurile gramaticale, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct p...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 21 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: What do the Portuguese artists’ stat..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 22 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 4: Which artist draws people’s attentio..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (4 puncte):**

Corectitudinea la nivel de competenţă lingvistică (componenta gramaticală şi ortografică) - 4 puncte. Utilizează, ortografiază corect modurile, timpurile, formele şi 0 1 2 3 4 structurile gramaticale, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct p...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 25 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: It is necessary to look after d) to ..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 26 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 4: Some Portuguese artists e) Roussel’s..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (4 puncte):**

Corectitudinea la nivel de competenţă lingvistică (componenta gramaticală şi ortografică) - 4 puncte. Utilizează, ortografiază corect modurile, timpurile, formele şi 0 1 2 3 4 structurile gramaticale, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct p...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 29 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: Art pieces made out of such material..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 32 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea Se acordă 5 puncte 2+3 5 puncte stilistică, alegerea pentru corespunderea 2 puncte pentru alegerea registrului stilistic adecvat textului produs. registrului stilistic textelor produse cu 3 puncte pentru respectarea normei stilistice a limbii rom...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 33 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte ortografice şi întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. numărul de greşeli gramaticale. ortografice sau • Se acordă 4 puncte, dacă au fost comise ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 34 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte de punctuaţie. întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. numărul de greşeli de • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. punctuaţie nu • Se acordă 3...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 43 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea Se acordă 5 puncte 2+3 5 puncte stilistică, alegerea pentru corespunderea 2 puncte pentru alegerea registrului stilistic adecvat textului produs. registrului stilistic textelor produse cu 3 puncte pentru respectarea normei stilistice a limbii rom...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 44 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte ortografice şi întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. numărul de greşeli gramaticale. ortografice sau • Se acordă 4 puncte, dacă au fost comise ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 45 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte de punctuaţie. întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. numărul de greşeli de • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. punctuaţie nu • Se acordă 3...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 48 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea Se acordă 5 puncte 2+3 5 puncte stilistică, alegerea pentru corespunderea 2 puncte pentru alegerea registrului stilistic adecvat textului produs. registrului stilistic textelor produse cu 3 puncte pentru respectarea normei stilistice a limbii rom...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 49 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte ortografice şi întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. numărul de greşeli gramaticale. ortografice sau • Se acordă 4 puncte, dacă au fost comise ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 50 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte de punctuaţie. întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. numărul de greşeli de • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. punctuaţie nu • Se acordă 3...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 63 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea Se acordă 5 puncte 2+3 5 puncte stilistică, alegerea pentru corespunderea 2 puncte pentru alegerea registrului stilistic adecvat textului produs. registrului stilistic textelor produse cu 3 puncte pentru respectarea normei stilistice a limbii rom...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 64 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte ortografice şi întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. numărul de greşeli gramaticale. ortografice sau • Se acordă 4 puncte, dacă au fost comise ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 65 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul 5 5 puncte de punctuaţie. întreg (5 puncte), dacă Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. numărul de greşeli de • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. punctuaţie nu • Se acordă 3...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 81 (istorie) -- match ratio 1.00
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 4: C..."

Span A: `1p. x2 – menționează două`

Span B: `1p. x2 – menționează două`

Full response: **Răspuns și explicație (1 puncte):**

Amplasarea în timp și spațiu a Amplasarea în timp (2 p) evenimentelor/proceselor/ 1p. x2 – menționează două date cronologice fenomenelor istorice. relevante. 4 puncte Amplasarea în spațiu (2) 1p. x2 – menționează două țări/ regiuni/ continente/ părți ale lumii....

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 86 (istorie) -- match ratio 1.00
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 4: D..."

Span A: `1p. x2 – menționează două`

Span B: `1p. x2 – menționează două`

Full response: **Răspuns și explicație (1 puncte):**

Amplasarea în timp și spațiu a Amplasarea în timp (2 p) evenimentelor/proceselor/ 1p. x2 – menționează două date cronologice fenomenelor istorice. relevante. 4 puncte Amplasarea în spațiu (2) 1p. x2 – menționează două țări/ regiuni/ continente/ părți ale lumii....

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 91 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 1: According to the text, people often ..."

Span A: `conform sarcinii indicate - 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) prezintă un/o edificiu/construcție/clădire dintr-o țară anglofonă, 0 1 conform sarcinii indicate - 1 p. b) numește țara anglofonă, conform sarcinii indicate - 1 p. 0 1 c) descrie edi...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 93 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: According to the text, if you want t..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 94 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 4: According to the text, people who us..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (4 puncte):**

Corectitudinea la nivel de competenţă lingvistică (componenta gramaticală şi ortografică) - 4 puncte. Utilizează, ortografiază corect modurile, timpurile, formele şi 0 1 2 3 4 structurile gramaticale, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct p...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 95 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 1: The word ‘average’ in the text means..."

Span A: `conform sarcinii indicate - 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) prezintă un/o edificiu/construcție/clădire dintr-o țară anglofonă, 0 1 conform sarcinii indicate - 1 p. b) numește țara anglofonă, conform sarcinii indicate - 1 p. 0 1 c) descrie edi...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 97 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 1: How much time does the average Ameri..."

Span A: `conform sarcinii indicate - 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) prezintă un/o edificiu/construcție/clădire dintr-o țară anglofonă, 0 1 conform sarcinii indicate - 1 p. b) numește țara anglofonă, conform sarcinii indicate - 1 p. 0 1 c) descrie edi...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 99 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: How long did the digital detox last ..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 100 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 4: Who can support a person during a so..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (4 puncte):**

Corectitudinea la nivel de competenţă lingvistică (componenta gramaticală şi ortografică) - 4 puncte. Utilizează, ortografiază corect modurile, timpurile, formele şi 0 1 2 3 4 structurile gramaticale, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct p...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 101 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 1: Too much social media use a) addicti..."

Span A: `conform sarcinii indicate - 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) prezintă un/o edificiu/construcție/clădire dintr-o țară anglofonă, 0 1 conform sarcinii indicate - 1 p. b) numește țara anglofonă, conform sarcinii indicate - 1 p. 0 1 c) descrie edi...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 103 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: The early stages of a social media o..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 104 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 4: Various screen-free activities conce..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (4 puncte):**

Corectitudinea la nivel de competenţă lingvistică (componenta gramaticală şi ortografică) - 4 puncte. Utilizează, ortografiază corect modurile, timpurile, formele şi 0 1 2 3 4 structurile gramaticale, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct p...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 105 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 1: Multiple studies have found that ove..."

Span A: `conform sarcinii indicate - 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) prezintă un/o edificiu/construcție/clădire dintr-o țară anglofonă, 0 1 conform sarcinii indicate - 1 p. b) numește țara anglofonă, conform sarcinii indicate - 1 p. 0 1 c) descrie edi...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 107 (limba_engleza) -- match ratio 1.00
Instruction: "Subiect: Limba engleză

Itemul 3: Many people who took part in digital..."

Span A: `puncte pentru respectarea volumului de`

Span B: `puncte pentru respectarea volumului de`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea la nivel de competență lingvistică (componenta lexicală şi ortografică) - 5 puncte. Posedă şi ortografiază corect vocabularul necesar pentru a descrie 0 1 2 3 4 5 subiectul propus, conform sarcinii indicate. N.B.1 Se va scădea câte 1 punct pentru...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 110 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea stilistică. Se acordă 5 puncte pentru 5 5 puncte respectarea normei stilistice Se va scădea câte 1 punct pentru fiecare 2 greşeli de exprimare. a limbii. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. • Se acordă 3 puncte, dacă au fost co...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 111 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul întreg (5 5 5 puncte ortografice şi puncte), dacă numărul de Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. greşeli ortografice sau gramaticale. gramaticale nu depăşeşte 1. • Se acordă 4 ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 112 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor de Se acordă punctajul întreg (5 5 5 puncte punctuaţie. puncte), dacă numărul de Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. greşeli de punctuaţie nu depăşeşte 1. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 122 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea stilistică. Se acordă 5 puncte pentru 5 5 puncte respectarea normei stilistice Se va scădea câte 1 punct pentru fiecare 2 greşeli de exprimare. a limbii. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. • Se acordă 3 puncte, dacă au fost co...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 123 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul întreg (5 5 5 puncte ortografice şi puncte), dacă numărul de Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. greşeli ortografice sau gramaticale. gramaticale nu depăşeşte 1. • Se acordă 4 ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 124 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor de Se acordă punctajul întreg (5 5 5 puncte punctuaţie. puncte), dacă numărul de Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. greşeli de punctuaţie nu depăşeşte 1. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 127 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea stilistică. Se acordă 5 puncte pentru 5 5 puncte respectarea normei stilistice Se va scădea câte 1 punct pentru fiecare 2 greşeli de exprimare. a limbii. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. • Se acordă 3 puncte, dacă au fost co...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 128 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul întreg (5 5 5 puncte ortografice şi puncte), dacă numărul de Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. greşeli ortografice sau gramaticale. gramaticale nu depăşeşte 1. • Se acordă 4 ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 129 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor de Se acordă punctajul întreg (5 5 5 puncte punctuaţie. puncte), dacă numărul de greşeli de punctuaţie nu Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. depăşeşte 1. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 142 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Corectitudinea stilistică. Se acordă 5 puncte pentru 5 5 puncte respectarea normei stilistice Se va scădea câte 1 punct pentru fiecare 2 greşeli de exprimare. a limbii. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. • Se acordă 3 puncte, dacă au fost co...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 143 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor Se acordă punctajul întreg (5 5 5 puncte ortografice şi puncte), dacă numărul de Se va scădea câte 1 punct pentru fiecare 2 greşeli ortografice sau gramaticale. greşeli ortografice sau gramaticale. gramaticale nu depăşeşte 1. • Se acordă 4 ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 144 (limba_romana) -- match ratio 1.00
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte, dacă au fost comise`

Span B: `puncte, dacă au fost comise`

Full response: **Răspuns și explicație (5 puncte):**

Respectarea normelor de Se acordă punctajul întreg (5 5 5 puncte punctuaţie. puncte), dacă numărul de greşeli de punctuaţie nu Se va scădea câte 1 punct pentru fiecare 2 greşeli de punctuaţie. depăşeşte 1. • Se acordă 4 puncte, dacă au fost comise 2-3 greşeli. ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 153 (matematica) -- match ratio 1.00
Instruction: "Subiect: Matematică (Profil Real)

Itemul 9: Studiați monotonia șirulu..."

Span A: `• aₙ₊₁ − aₙ =`

Span B: `• aₙ₊₁ − aₙ =`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• aₙ₊₁ − aₙ = (2n+3)/(n+2) − (2n+1)/(n+1)
• Numărător după aducere la numitor comun: 1
• aₙ₊₁ − aₙ = 1/[(n+2)(n+1)] > 0
• Șirul este strict crescător
• Punctaj: 5 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 113 (limba_romana) -- match ratio 0.97
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `pentru cunoaștere în textul dat,`

Span B: `pentru cunoaștere în textul dat;`

Full response: **Răspuns și explicație (6 puncte):**

Analizează, în spațiul rezervat, Se va accepta un răspuns în care: 2+1+2+1 6 puncte motivul literar al pasiunii - este relevată semnificaţia motivului literar al pasiunii 2 puncte pentru relevarea semnificaţiei pentru cunoaștere în textul dat, pentru cunoaștere...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 13 (limba_engleza) -- match ratio 0.97
Instruction: "Subiect: Limba engleză

Itemul 1: According to the text, popular forms..."

Span A: `conform sarcinii indicate 0 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) identifică/numește autorul/autoarea, conform sarcinii indicate 0 1 - 1 p. b) prezintă țara anglofonă, conform sarcinii indicate - 1 p. 0 1 0 3 6 c) prezintă/descrie aspecte ale opere...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 17 (limba_engleza) -- match ratio 0.97
Instruction: "Subiect: Limba engleză

Itemul 1: The word ‘message’ in the text is cl..."

Span A: `conform sarcinii indicate 0 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) identifică/numește autorul/autoarea, conform sarcinii indicate 0 1 - 1 p. b) prezintă țara anglofonă, conform sarcinii indicate - 1 p. 0 1 0 3 6 c) prezintă/descrie aspecte ale opere...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 19 (limba_engleza) -- match ratio 0.97
Instruction: "Subiect: Limba engleză

Itemul 1: What materials does Małgorzata Choda..."

Span A: `conform sarcinii indicate 0 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) identifică/numește autorul/autoarea, conform sarcinii indicate 0 1 - 1 p. b) prezintă țara anglofonă, conform sarcinii indicate - 1 p. 0 1 0 3 6 c) prezintă/descrie aspecte ale opere...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 23 (limba_engleza) -- match ratio 0.97
Instruction: "Subiect: Limba engleză

Itemul 1: Some sculptors use water b) is not v..."

Span A: `conform sarcinii indicate 0 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) identifică/numește autorul/autoarea, conform sarcinii indicate 0 1 - 1 p. b) prezintă țara anglofonă, conform sarcinii indicate - 1 p. 0 1 0 3 6 c) prezintă/descrie aspecte ale opere...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 27 (limba_engleza) -- match ratio 0.97
Instruction: "Subiect: Limba engleză

Itemul 1: The Portuguese artists’ creations ha..."

Span A: `conform sarcinii indicate 0 1`

Span B: `conform sarcinii indicate - 1`

Full response: **Răspuns și explicație (16 puncte):**

Corectitudinea la nivel de competență culturală şi pragmatică – 16 puncte. a) identifică/numește autorul/autoarea, conform sarcinii indicate 0 1 - 1 p. b) prezintă țara anglofonă, conform sarcinii indicate - 1 p. 0 1 0 3 6 c) prezintă/descrie aspecte ale opere...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 51 (limba_romana) -- match ratio 0.96
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `a referință directă la text.`

Span B: `o referință directă la text.`

Full response: **Răspuns și explicație (4 puncte):**

Explică, în 2-3 enunțuri, starea eului Se va accepta răspunsul în care este reperată 1+2+1 4 puncte liric, exprimată în versurile din text. una dintre stările eului liric (reculegere, 1 punct pentru nominalizarea unei stări a îndurerare, dorința de mângâiere ma...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 53 (limba_romana) -- match ratio 0.96
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `portretul moral al personajului -`

Span B: `portretul moral al personajului, 1`

Full response: **Răspuns și explicație (6 puncte):**

Schițează, într-un text coerent de 6-7 Se va accepta un text coerent în care: 1+2+2+1 6 puncte rânduri, portretul moral al personajului - se schițează portretul moral al personajului, 1 punct pentru că textul se referă la Nichita, indicând două trăsături indicâ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 130 (limba_romana) -- match ratio 0.93
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `figurii de stil analizate. 2`

Span B: `a figurii de stil analizate.`

Full response: **Răspuns și explicație (5 puncte):**

Comentează, în text coerent de 6- Se va accepta un răspuns în care: 1+1+1+2 5 puncte 7 rânduri, sugestia contextuală a - este rescrisă complet figura de stil; 1 punct pentru rescrierea completă a figurii unei figuri de stil din fragmentul - este nominalizată fi...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 37 (limba_romana) -- match ratio 0.92
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `valența stilistică a semnelor de`

Span B: `valenței stilistice a semnelor de`

Full response: **Răspuns și explicație (4 puncte):**

Interpretează, în două Se va accepta un răspuns în care: 2+2 4 puncte enunțuri dezvoltate, valoarea - este identificată tipologia enunţurilor vizate 2 puncte (1+1) pentru identificarea stilistică a semnului de (exclamativ; interogativ); tipului de enunţ; exclam...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 136 (limba_romana) -- match ratio 0.88
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `1 punct pentru denumirea documentului;`

Span B: `1 punct pentru denumirea evenimentului;`

Full response: **Răspuns și explicație (7 puncte):**

Scrie un anunț, valorificând Se va accepta textul unui anunț despre 1+1+1+1+1+1+1 7 puncte datele legendei: „Te numești lansarea Ghidului: 1 punct pentru denumirea documentului; Ion/Ioana Moraru. Studiezi la denumirea evenimentului, timpul, locul Liceul Teoreti...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 75 (matematica) -- match ratio 0.88
Instruction: "Subiect: Matematică (Profil Real)

Itemul 10: Fie funcția f: [−π/2; π/..."

Span A: `• lim f(x)/x = lim`

Span B: `• lim f(x)/(x²+x) = lim`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• lim f(x)/x = lim [sin(2x)/x − 1] = 2 − 1 = 1
• lim f(x)/(x²+x) = lim f(x)/[x(x+1)] = 1/1 = 1
• Punctaj: 8 puncte (subpunctele a, b, c)...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 31 (limba_romana) -- match ratio 0.88
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `întreg (3 puncte), dacă Se`

Span B: `întreg (3 puncte), dacă textele`

Full response: **Răspuns și explicație (3 puncte):**

Calitatea mesajului Se acordă punctajul 3 3 puncte scris: coerență și întreg (3 puncte), dacă Se acordă punctajul întreg (3 puncte), dacă textele produse sunt coerente. coeziune. textele produse sunt Se acordă 2 puncte, dacă se atestă anumite (1-2) carenţe de o...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 42 (limba_romana) -- match ratio 0.88
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `întreg (3 puncte), dacă Se`

Span B: `întreg (3 puncte), dacă textele`

Full response: **Răspuns și explicație (3 puncte):**

Calitatea mesajului Se acordă punctajul 3 3 puncte scris: coerență și întreg (3 puncte), dacă Se acordă punctajul întreg (3 puncte), dacă textele produse sunt coerente. coeziune. textele produse sunt Se acordă 2 puncte, dacă se atestă anumite (1-2) carenţe de o...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 47 (limba_romana) -- match ratio 0.88
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `întreg (3 puncte), dacă Se`

Span B: `întreg (3 puncte), dacă textele`

Full response: **Răspuns și explicație (3 puncte):**

Calitatea mesajului Se acordă punctajul 3 3 puncte scris: coerență și întreg (3 puncte), dacă Se acordă punctajul întreg (3 puncte), dacă textele produse sunt coerente. coeziune. textele produse sunt Se acordă 2 puncte, dacă se atestă anumite (1-2) carenţe de o...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 62 (limba_romana) -- match ratio 0.88
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `întreg (3 puncte), dacă Se`

Span B: `întreg (3 puncte), dacă textele`

Full response: **Răspuns și explicație (3 puncte):**

Calitatea mesajului Se acordă punctajul 3 3 puncte scris: coerență și întreg (3 puncte), dacă Se acordă punctajul întreg (3 puncte), dacă textele produse sunt coerente. coeziune. textele produse sunt Se acordă 2 puncte, dacă se atestă anumite (1-2) carenţe de o...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 139 (limba_romana) -- match ratio 0.88
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `pentru exprimarea clară a opiniei;`

Span B: `a) exprimarea clară a opiniei;`

Full response: **Răspuns și explicație (2 puncte):**

Redactează un eseu argumentativ Se va accepta un eseu argumentativ în 2+4+4+6+3+1 20 de puncte de 1-1,5 pagini, în raport cu care s-a valorificat următorul algoritm: 2 puncte pentru exprimarea clară a opiniei; aserțiunea: Nu poți deschide o a) exprimarea clară ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 54 (limba_romana) -- match ratio 0.87
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `al demnității în textul dat;`

Span B: `al demnității în textul dintr-un`

Full response: **Răspuns și explicație (6 puncte):**

Analizează, într-un text coerent de 5-6 Se va accepta un răspuns în care: 2+1+2+1 6 puncte rânduri, motivul literar al demnității - este relevată semnificaţia motivului literar 2 puncte pentru relevarea semnificaţiei în textul dat, în raport cu același motiv al...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 119 (limba_romana) -- match ratio 0.86
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `exprimarea clară a opiniei. puncte`

Span B: `exprimarea clară a opiniei; (Se`

Full response: **Răspuns și explicație (2 puncte):**

Redactează un eseu argumentativ Se va accepta un eseu argumentativ în care s-au realizat 2+4+4+6+3+1 20 de de 1-1,5 pagini, în raport cu următoarele: 2 puncte pentru exprimarea clară a opiniei. puncte aserțiunea: Valoarea unui om nu a) exprimarea clară a opinie...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 52 (limba_romana) -- match ratio 0.86
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `complet figura de stil 1`

Span B: `completă a figuri de stil`

Full response: **Răspuns și explicație (5 puncte):**

Comentează, în text coerent de 5-6 Se va accepta un răspuns în care: 1+1+1+2 5 puncte rânduri, sugestia contextuală a unei - este rescrisă complet figura de stil 1 punct pentru rescrierea completă a figuri de stil din versurile inserate în nominalizată; figurii...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 109 (limba_romana) -- match ratio 0.86
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `1 punct pentru utilizarea de`

Span B: `1 punct pentru abilitatea de`

Full response: **Răspuns și explicație (3 puncte):**

Aptitudini de analiză şi Se acordă pentru dovada 3 3 puncte de interpretări critice. capacităţii de Cele 3 puncte vor fi distribuite astfel: analiză/comentare a textului propus și a textelor alese 1 punct pentru constatarea aspectelor definitorii ale sarcinilor...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 121 (limba_romana) -- match ratio 0.86
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `1 punct pentru utilizarea de`

Span B: `1 punct pentru abilitatea de`

Full response: **Răspuns și explicație (3 puncte):**

Aptitudini de analiză şi Se acordă pentru dovada 3 3 puncte de interpretări critice. capacităţii de Cele 3 puncte vor fi distribuite astfel: analiză/comentare a textului propus și a textelor alese 1 punct pentru constatarea aspectelor definitorii ale sarcinilor...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 126 (limba_romana) -- match ratio 0.86
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `1 punct pentru utilizarea de`

Span B: `1 punct pentru abilitatea de`

Full response: **Răspuns și explicație (3 puncte):**

Aptitudini de analiză şi Se acordă pentru dovada 3 3 puncte de interpretări critice. capacităţii de Cele 3 puncte vor fi distribuite astfel: analiză/comentare a textului propus și a textelor alese 1 punct pentru constatarea aspectelor definitorii ale sarcinilor...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 141 (limba_romana) -- match ratio 0.86
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `1 punct pentru utilizarea de`

Span B: `1 punct pentru abilitatea de`

Full response: **Răspuns și explicație (3 puncte):**

Aptitudini de analiză şi Se acordă pentru dovada 3 3 puncte de interpretări critice. capacităţii de Cele 3 puncte vor fi distribuite astfel: analiză/comentare a textului propus și a textelor alese 1 punct pentru constatarea aspectelor definitorii ale sarcinilor...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 150 (matematica) -- match ratio 0.86
Instruction: "Subiect: Matematică (Profil Real)

Itemul 6: Într-un cilindru circular..."

Span A: `r = 2 cm •`

Span B: `2r = 4 cm •`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• πr² = 4π ⟹ r = 2 cm
• h = 2r = 4 cm
• V = πr²h = 16π cm³
• Punctaj: 5 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 74 (matematica) -- match ratio 0.85
Instruction: "Subiect: Matematică (Profil Real)

Itemul 9: Studiați paritatea funcți..."

Span A: `= (−x)³ + 1/(−x) =`

Span B: `= −(x³ + 1/x) =`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• f(−x) = (−x)³ + 1/(−x) = −x³ − 1/x = −(x³ + 1/x) = −f(x)
• f(−x) = −f(x) ⟹ funcția este impară
• Punctaj: 5 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 149 (matematica) -- match ratio 0.85
Instruction: "Subiect: Matematică (Profil Real)

Itemul 5: Determinați valorile real..."

Span A: `≠ 0 • sinα(1/cosα +`

Span B: `≠ 0 • 1/cosα +`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• det(A) = tgα + 2sinα ≠ 0
• sinα(1/cosα + 2) ≠ 0
• 1/cosα + 2 = 0 ⟹ cosα = −1/2 ⟹ α = 4π/3
• Răspuns: α ∈ (π; 7π/4) \ {3π/2; 4π/3}
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 146 (matematica) -- match ratio 0.85
Instruction: "Subiect: Matematică (Profil Real)

Itemul 2: Fie z = (3−i)/(1+3i), und..."

Span A: `• Numărător: (3−i)(1−3i) = −10i`

Span B: `• Numitor: (1+3i)(1−3i) = 10`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• Se amplifică cu (1−3i):
• Numărător: (3−i)(1−3i) = −10i
• Numitor: (1+3i)(1−3i) = 10
• z = −i (pur imaginar, partea reală = 0) ✓
• Punctaj: 5 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 38 (limba_romana) -- match ratio 0.84
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `2 puncte pentru indicarea timpului`

Span B: `1 punct pentru indicarea locului;`

Full response: **Răspuns și explicație (10 puncte):**

Elaborează, în spațiul Se va accepta textul unei invitații la ședința Clubului 1+2+2+1+1+1+1+1 10 puncte rezervat, o invitație adresată de lectură cu date din legendă: denumirea textului, 1 punct pentru adresarea către invitat; scriitorului Vladimir numele scr...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 117 (limba_romana) -- match ratio 0.84
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `2 puncte pentru indicarea timpului`

Span B: `1 punct pentru indicarea locului.`

Full response: **Răspuns și explicație (10 puncte):**

Scrie, în spațiul rezervat, o Se va accepta textul unei invitații cu respectarea datelor din 1+1+2+1+2+1+1+1 10 puncte invitație pe care o vei adresa legendă: 1 punct pentru prezența formulei de colegilor tăi, valorificând datele - utilizarea convențiilor spec...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 137 (limba_romana) -- match ratio 0.83
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `puncte punct de vedere cu`

Span B: `un punct de vedere care`

Full response: **Răspuns și explicație (4 puncte):**

Exprimă, în spaţiul rezervat, un Se va accepta un răspuns în care: 2+2 4 puncte punct de vedere cu privire la - este formulat un punct de vedere care 2 puncte pentru exprimarea punctului de necesitatea de a-ți păstra calmul vizează problema enunțată; vedere; în...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 118 (limba_romana) -- match ratio 0.82
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `un punct de vedere prin`

Span B: `un punct de vedere referitor`

Full response: **Răspuns și explicație (6 puncte):**

Formulează, în text coerent de 7- Se va accepta un răspuns în care: 2+2+1+1 6 puncte 8 rânduri, un punct de vedere prin - este formulat un punct de vedere referitor la problema 2 puncte pentru formularea punctului de care să argumentezi dacă enunțată; vedere. î...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 56 (limba_romana) -- match ratio 0.82
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `4 puncte de vedere cu`

Span B: `un punct de vedere care`

Full response: **Răspuns și explicație (4 puncte):**

Exprimă, în spaţiul rezervat, un punct Se va accepta un răspuns în care: 2+2 4 puncte de vedere cu privire la importanța - este formulat un punct de vedere care 2 puncte pentru exprimarea punctului de sprijinului moral de care are nevoie o vizează problema enun...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 36 (limba_romana) -- match ratio 0.81
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `motivul literar al - este`

Span B: `motivului literar al 2 puncte`

Full response: **Răspuns și explicație (6 puncte):**

Analizează, în spațiul Se va accepta un răspuns în care: 2+1+2+1 6 puncte rezervat, motivul literar al - este relevată semnificaţia motivului literar al 2 puncte pentru relevarea semnificaţiei verticalității morale în textul verticalității morale în textul dat;...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 60 (limba_romana) -- match ratio 0.81
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `un eseu argumentativ de 1-`

Span B: `un eseu argumentativ în care`

Full response: **Răspuns și explicație (2 puncte):**

Redactează un eseu argumentativ de 1- Se va accepta un eseu argumentativ în care s- 2+4+4+6+3+1 20 de 1,5 pagini, în raport cu ideea din text: au realizat următoarele: 2 puncte pentru exprimarea clară a puncte Dragostea-i văzduhul fără de care nici a) exprimare...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 58 (limba_romana) -- match ratio 0.81
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `textului la genul dramatic. apartenenţa`

Span B: `textului la genul dramatic, de`

Full response: **Răspuns și explicație (4 puncte):**

Argumentează, în două teze Se vor accepta două teze construite corect: 2+2 4 puncte (raționament + exemplu) apartenența raţionament+exemplu, ce demonstrează 2 (1+1) puncte pentru raţionamente textului la genul dramatic. apartenenţa textului la genul dramatic, d...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 132 (limba_romana) -- match ratio 0.81
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `1 punct pentru că textul`

Span B: `1 punct pentru coerența textului.`

Full response: **Răspuns și explicație (6 puncte):**

Schițează, în spațiul rezervat, Se va accepta un text coerent în care: 2+2+1+1 6 puncte portretul moral al bătrânului - este schițat portretul moral al 2 (1+1) puncte pentru identificarea corectă ceasornicar, indicând două personajului, indicându-se două a trăs...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 72 (matematica) -- match ratio 0.80
Instruction: "Subiect: Matematică (Profil Real)

Itemul 7: În triunghiul isoscel ABC..."

Span A: `• AC = 20 cm`

Span B: `⟹ AB = 20 cm,`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• Teorema bisectoarei: AB/BC = AD/DC = 2/3
• AC = 20 cm ⟹ AB = 20 cm, BC = 30 cm
• Se calculează înălțimea din datele obținute
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 30 (limba_romana) -- match ratio 0.78
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `claritatea ideilor — 1 punct;`

Span B: `consecutivitatea ideilor — 1 punct.`

Full response: **Răspuns și explicație (2 puncte):**

Structurarea adecvată Se acordă în cazul 2 2 puncte a textului propriu. unei lucrări Cele 2 puncte vor fi distribuite după principiul calitativ: (se referă la eseul din structurate, cu • claritatea ideilor — 1 punct; i temul 12). distincţiile clare între • cons...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 41 (limba_romana) -- match ratio 0.78
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `claritatea ideilor — 1 punct;`

Span B: `consecutivitatea ideilor — 1 punct.`

Full response: **Răspuns și explicație (2 puncte):**

Structurarea adecvată Se acordă în cazul 2 2 puncte a textului propriu. unei lucrări Cele 2 puncte vor fi distribuite după principiul calitativ: (se referă la eseul din structurate, cu • claritatea ideilor — 1 punct; i temul 12). distincţiile clare între • cons...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 46 (limba_romana) -- match ratio 0.78
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `claritatea ideilor — 1 punct;`

Span B: `consecutivitatea ideilor — 1 punct.`

Full response: **Răspuns și explicație (2 puncte):**

Structurarea adecvată Se acordă în cazul 2 2 puncte a textului propriu. unei lucrări Cele 2 puncte vor fi distribuite după principiul calitativ: (se referă la eseul din structurate, cu • claritatea ideilor — 1 punct; i temul 15). distincţiile clare între • cons...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 61 (limba_romana) -- match ratio 0.78
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `claritatea ideilor — 1 punct;`

Span B: `consecutivitatea ideilor — 1 punct.`

Full response: **Răspuns și explicație (2 puncte):**

Structurarea adecvată Se acordă în cazul 2 2 puncte a textului propriu. unei lucrări Cele 2 puncte vor fi distribuite după principiul calitativ: (se referă la eseul din structurate, cu • claritatea ideilor — 1 punct; i temul 15). distincţiile clare între • cons...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 40 (limba_romana) -- match ratio 0.78
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `e i n d e`

Span B: `p e n d e`

Full response: **Răspuns și explicație (2 puncte):**

Redactează un eseu Se va accepta un eseu argumentativ în care s-au 2+4+4+6+3+1 20 de argumentativ de 1–1,5 pagini, realizat următoarele: 2 puncte pentru exprimarea clară a puncte în raport cu aserțiunea lui a) exprimarea clară a opiniei; opiniei; Aristotel: Dem...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 156 (matematica) -- match ratio 0.78
Instruction: "Subiect: Matematică (Profil Real)

Itemul 12: Suma coeficienților bino..."

Span A: `⟹ n = 9 •`

Span B: `⟹ k = 6 •`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• 2^(n−1) = 256 = 2^8 ⟹ n = 9
• T(k+1) = C(9,k)·x^((9-k)/3 − k/2)
• (9−k)/3 − k/2 = −2 ⟹ k = 6
• Coeficient = C(9,6) = 84
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 35 (limba_romana) -- match ratio 0.77
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `2 puncte pentru fiecare citat`

Span B: `(1 punct pentru adecvarea citatului;`

Full response: **Răspuns și explicație (5 puncte):**

Determină, în text coerent de Se va accepta un răspuns în care: 1+2+2 5 puncte 6-7 rânduri, atitudinea - este determinată atitudinea colegilor (dezaprobare, 1 punct pentru determinarea atitudinii colegilor față de tânărul poet, invidie, blamare, ostilitate etc....

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 114 (limba_romana) -- match ratio 0.77
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `2 puncte pentru fiecare citat`

Span B: `(1 punct pentru adecvarea citatului;`

Full response: **Răspuns și explicație (6 puncte):**

Determină, în text coerent de 5-6 Se va accepta un răspuns în care: 1+2+2+1 6 puncte rânduri, atitudinea personajului- - este determinată atitudinea personajului: atitudine 1 punct pentru determinarea atitudinii (care narator față de profesorul Hilbert, respect...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 115 (limba_romana) -- match ratio 0.76
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `Eu, mâine- Punctele de suspensie`

Span B: `a a punctelor de suspensie`

Full response: **Răspuns și explicație (3 puncte):**

Interpretează, în spațiul rezervat, Se va accepta un răspuns în care: 1+2 3 puncte valoarea stilistică a punctelor de - este elucidată utilizarea gramaticală a semnului de 1 punct pentru motivarea utilizării suspensie din secvența propusă: punctuație; gramatica...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 59 (limba_romana) -- match ratio 0.76
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `invitația. 2 puncte pentru indicarea`

Span B: `(câte 1 punct pentru indicarea`

Full response: **Răspuns și explicație (7 puncte):**

Elaborează, în spațiul rezervat, o Se va accepta textul unei invitații cu 4+3 7 puncte invitație pe care o vei adresa colegilor respectarea datelor din legendă: 4 puncte (1+1+1+1) tăi, valorificând datele legendei: „Te - utilizarea convențiilor specifice acestu...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 108 (limba_romana) -- match ratio 0.76
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `întindere. respectând limita de întindere.`

Span B: `pentru respectarea limitei de întindere.`

Full response: **Răspuns și explicație (2 puncte):**

Organizarea în scris a Se acordă în cazul unei 2 2 puncte ideilor şi respectarea lucrări structurate coerent, Cele 2 puncte vor fi distribuite astfel: limitei de întindere. respectând limita de întindere. - 1 punct pentru claritatea şi consecutivitatea ideilor;...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 120 (limba_romana) -- match ratio 0.76
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `întindere. respectând limita de întindere.`

Span B: `pentru respectarea limitei de întindere.`

Full response: **Răspuns și explicație (2 puncte):**

Organizarea în scris a Se acordă în cazul unei 2 2 puncte ideilor şi respectarea lucrări structurate coerent, Cele 2 puncte vor fi distribuite astfel: limitei de întindere. respectând limita de întindere. - 1 punct pentru claritatea şi consecutivitatea ideilor;...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 125 (limba_romana) -- match ratio 0.76
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `întindere. respectând limita de întindere.`

Span B: `pentru respectarea limitei de întindere.`

Full response: **Răspuns și explicație (2 puncte):**

Organizarea în scris a Se acordă în cazul unei 2 2 puncte ideilor şi respectarea lucrări structurate coerent, Cele 2 puncte vor fi distribuite astfel: limitei de întindere. respectând limita de întindere. - 1 punct pentru claritatea şi consecutivitatea ideilor;...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 140 (limba_romana) -- match ratio 0.76
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `întindere. respectând limita de întindere.`

Span B: `pentru respectarea limitei de întindere.`

Full response: **Răspuns și explicație (2 puncte):**

Organizarea în scris a Se acordă în cazul unei 2 2 puncte ideilor şi respectarea lucrări structurate coerent, Cele 2 puncte vor fi distribuite astfel: limitei de întindere. respectând limita de întindere. - 1 punct pentru claritatea şi consecutivitatea ideilor;...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 131 (limba_romana) -- match ratio 0.75
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `atitudinea naratoarei față - este`

Span B: `atitudinea naratoarei 1 punct pentru`

Full response: **Răspuns și explicație (3 puncte):**

Determină, în text coerent de 5-6 Se va accepta un răspuns în care: 1+2 3 puncte rânduri, atitudinea naratoarei față - este determinată atitudinea naratoarei 1 punct pentru determinarea atitudinii (care de Sebastian, angajând un citat din fragmentul propus. (de...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 69 (matematica) -- match ratio 0.74
Instruction: "Subiect: Matematică (Profil Real)

Itemul 4: Determinați valorile real..."

Span A: `+ m = 0 •`

Span B: `• m = 18 •`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• z = a+ai ⟹ z² = 2a²i
• Substituție: 2a²i − 6(a+ai) + m = 0
• Partea reală: m = 6a; Partea imaginară: a = 3
• m = 18
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 133 (limba_romana) -- match ratio 0.72
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `construite 2+2 4 puncte (raționament+exemplu),`

Span B: `corect (raționament + exemplu), ce`

Full response: **Răspuns și explicație (4 puncte):**

Argumentează, în două teze Se vor accepta două teze construite 2+2 4 puncte (raționament+exemplu), corect (raționament + exemplu), ce 2 (1+1) puncte pentru raționamente corecte; apartenența fragmentului dat la demonstrează apartenența textului la genul epic. g ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 70 (matematica) -- match ratio 0.72
Instruction: "Subiect: Matematică (Profil Real)

Itemul 5: Rezolvați în ℝ inecuația:..."

Span A: `(3t²−4t+1)·√(1−x) ≤ 0 • Factorizare:`

Span B: `(3t−1)(t−1)·√(1−x) ≤ 0 • Condiție`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• Substituție t = 3^x: (3t²−4t+1)·√(1−x) ≤ 0
• Factorizare: (3t−1)(t−1)·√(1−x) ≤ 0
• Condiție domeniu: x ≤ 1
• Se analizează semnul pe intervale
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 68 (matematica) -- match ratio 0.71
Instruction: "Subiect: Matematică (Profil Real)

Itemul 3: Rezolvați în ℝ ecuația: l..."

Span A: `2 • log[(x−1)(x−2)] = 1`

Span B: `⟹ (x−1)(x−2) = 10 •`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• Condiții: x > 2
• log[(x−1)(x−2)] = 1 ⟹ (x−1)(x−2) = 10
• x² − 3x − 8 = 0
• Se selectează soluția cu x > 2
• 2 puncte pentru rezolvare corectă...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 71 (matematica) -- match ratio 0.71
Instruction: "Subiect: Matematică (Profil Real)

Itemul 6: Punctele A, B, C aparțin ..."

Span A: `− 100° = 80° •`

Span B: `× 80° = 160° •`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• ∠ABC = 180° − 100° = 80°
• Arc AC = 2 × 80° = 160°
• Punctaj: 5 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 57 (limba_romana) -- match ratio 0.69
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `mai rar. 2 puncte pentru`

Span B: `afirmației date; 1 punct pentru`

Full response: **Răspuns și explicație (4 puncte):**

Meditează, în text coerent de 6-7 Se va accepta un text cu caracter de meditaţie 1+2+1 4 puncte rânduri, asupra afirmației din replica lui asupra afirmației. 1 punct pentru caracterul meditativ al Nichita: Dar poeții geniali se nasc o textului produs; data la o...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 0 (istorie) -- match ratio 0.69
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Context:
SU..."

Span A: `argumentele abordează tangențial tema independenții`

Span B: `argumentele dezvoltă tema propusă. independenței`

Full response: **Răspuns și explicație (6 puncte):**

Utilizează sursele și cunoștințele Formulează trei argumente (6p.) obținute anterior pentru a redacta, 0 p. – răspuns lipsă/ greșit; 10 puncte într-o pagină, un eseu la tema: 1 p.X3 – argument parțial/declarativ; 2 p.X3 – argument construit corect Provocări și ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 5 (istorie) -- match ratio 0.69
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 1: I..."

Span A: `argumentele abordează tangențial tema independenții`

Span B: `argumentele dezvoltă tema propusă. independenței`

Full response: **Răspuns și explicație (6 puncte):**

Utilizează sursele și cunoștințele Formulează trei argumente (6p.) obținute anterior pentru a redacta, 0 p. – răspuns lipsă/ greșit; 10 puncte într-o pagină, un eseu la tema: 1 p.X3 – argument parțial/declarativ; 2 p.X3 – argument construit corect Provocări și ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 10 (istorie) -- match ratio 0.69
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 1: N..."

Span A: `argumentele abordează tangențial tema independenții`

Span B: `argumentele dezvoltă tema propusă. independenței`

Full response: **Răspuns și explicație (6 puncte):**

Utilizează sursele și cunoștințele Formulează trei argumente (6p.) obținute anterior pentru a redacta, 0 p. – răspuns lipsă/ greșit; 10 puncte într-o pagină, un eseu la tema: 1 p.X3 – argument parțial/declarativ; 2 p.X3 – argument construit corect Provocări și ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 39 (limba_romana) -- match ratio 0.68
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL – 100 de pun..."

Span A: `unui aspect/detaliu referindu-te la propria`

Span B: `puncte pentru referinţă la propria`

Full response: **Răspuns și explicație (6 puncte):**

Formulează, în text coerent Se va accepta un răspuns în care: 2+2+2 6 puncte de 7-8 rânduri, un punct de - este formulat un punct de vedere concludent 2 puncte pentru exprimarea unui punct vedere prin care să (pertinent, plauzibil) referitor la problema enunțat...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 147 (matematica) -- match ratio 0.67
Instruction: "Subiect: Matematică (Profil Real)

Itemul 3: Rezolvați în ℝ ecuația: 2..."

Span A: `⟹ x = ±2/3 •`

Span B: `0: S = {−2/3} •`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• Condiție: x ≤ 0 și 1−2x² ≥ 0
• Se ridică la pătrat: 4(1−2x²) = x²
• 9x² = 4 ⟹ x = ±2/3
• Se selectează x ≤ 0: S = {−2/3}
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 116 (limba_romana) -- match ratio 0.65
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL REAL –100 de punc..."

Span A: `pentru a califica textul dat`

Span B: `text, care califică fragmentul dat`

Full response: **Răspuns și explicație (4 puncte):**

Prezintă două argumente, Se va accepta un răspuns care conţine: 2+2 4 puncte ilustrate cu câte o secvenţă din - două argumente pentru a califica textul dat ca pe o 2 puncte (1+1) pentru formularea corectă a text, care califică fragmentul dat narațiune (narator,...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 152 (matematica) -- match ratio 0.64
Instruction: "Subiect: Matematică (Profil Real)

Itemul 8: Baza unei piramide este u..."

Span A: `= 12 cm • tg60°`

Span B: `h = 12√3 cm •`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• Latura rombului: a = √(15²+20²) = 25 cm
• Raza cercului înscris: r = (30·40)/(4·25) = 12 cm
• tg60° = h/r ⟹ h = 12√3 cm
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 78 (istorie) -- match ratio 0.64
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Context:
SU..."

Span A: `tema: 1 p.X3 – argument`

Span B: `2 p.X3 – argument construit`

Full response: **Răspuns și explicație (6 puncte):**

Utilizează sursele și cunoștințele Formulează trei argumente (6p.) obținute anterior pentru a redacta, 0 p. – răspuns lipsă/ greșit; 10 puncte într-o pagină, un eseu la tema: 1 p.X3 – argument parțial/declarativ; 2 p.X3 – argument construit corect A reușit Mare...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 83 (istorie) -- match ratio 0.64
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 1: I..."

Span A: `tema: 1 p.X3 – argument`

Span B: `2 p.X3 – argument construit`

Full response: **Răspuns și explicație (6 puncte):**

Utilizează sursele și cunoștințele Formulează trei argumente (6p.) obținute anterior pentru a redacta, 0 p. – răspuns lipsă/ greșit; 10 puncte într-o pagină, un eseu la tema: 1 p.X3 – argument parțial/declarativ; 2 p.X3 – argument construit corect A reușit Mare...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 88 (istorie) -- match ratio 0.64
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 1: I..."

Span A: `tema: 1 p.X3 – argument`

Span B: `2 p.X3 – argument construit`

Full response: **Răspuns și explicație (6 puncte):**

Utilizează sursele și cunoștințele Formulează trei argumente (6p.) obținute anterior pentru a redacta, 0 p. – răspuns lipsă/ greșit; 10 puncte într-o pagină, un eseu la tema: 1 p.X3 – argument parțial/declarativ; 2 p.X3 – argument construit corect A reușit Mare...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 151 (matematica) -- match ratio 0.64
Instruction: "Subiect: Matematică (Profil Real)

Itemul 7: Fie triunghiul isoscel AB..."

Span A: `MN = 15 cm •`

Span B: `· 6 = 105 cm²`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• Înălțimea din B: h_B = √(26²−10²) = 24 cm
• Raport asemănare: 18/24 = 3/4 ⟹ MN = 15 cm
• Înălțimea trapezului = 24−18 = 6 cm
• Aria = (20+15)/2 · 6 = 105 cm²
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 55 (limba_romana) -- match ratio 0.64
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANIST – 100 de ..."

Span A: `valorii de punctuație: puncte-puncte (a`

Span B: `punctuație: puncte-puncte (puncte de gramaticale;`

Full response: **Răspuns și explicație (3 puncte):**

Interpretează, în două enunțuri Se va accepta un răspuns în care este 1+2 3 puncte dezvoltate, valoarea stilistică a semnului elucidată utilizarea gramaticală a semnului de 1 punct pentru elucidarea valorii de punctuație: puncte-puncte (a punctuație: puncte-pun...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 2 (istorie) -- match ratio 0.62
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Context:
SU..."

Span A: `fără a face trimitere la`

Span B: `fără a fi integrat în`

Full response: **Răspuns și explicație (4 puncte):**

Integrează critic informațiile din Integrează critic(4p.) sursele propuse în propriul text. 0 p. - răspuns lipsă sau fără a face trimitere la surse; textul surselor este preluat fără a fi integrat în text; 1 p. – se fac unele încercări de a cita, de a face trim...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 7 (istorie) -- match ratio 0.62
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 3: D..."

Span A: `fără a face trimitere la`

Span B: `fără a fi integrat în`

Full response: **Răspuns și explicație (4 puncte):**

Integrează critic informațiile din Integrează critic(4p.) sursele propuse în propriul text. 0 p. - răspuns lipsă sau fără a face trimitere la surse; textul surselor este preluat fără a fi integrat în text; 1 p. – se fac unele încercări de a cita, de a face trim...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 12 (istorie) -- match ratio 0.62
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 3: F..."

Span A: `fără a face trimitere la`

Span B: `fără a fi integrat în`

Full response: **Răspuns și explicație (4 puncte):**

Integrează critic informațiile din Integrează critic(4p.) sursele propuse în propriul text. 0 p. - răspuns lipsă sau fără a face trimitere la surse; textul surselor este preluat fără a fi integrat în text; 1 p. – se fac unele încercări de a cita, de a face trim...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 80 (istorie) -- match ratio 0.62
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 3: D..."

Span A: `fără a face trimitere la`

Span B: `fără a fi integrat în`

Full response: **Răspuns și explicație (4 puncte):**

Integrează critic informațiile din Integrează critic(4p.) sursele propuse în propriul text. 0 p. - răspuns lipsă sau fără a face trimitere la surse; textul surselor este preluat fără a fi integrat în text; 1 p. – se fac unele încercări de a cita, de a face trim...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 85 (istorie) -- match ratio 0.62
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 3: D..."

Span A: `fără a face trimitere la`

Span B: `fără a fi integrat în`

Full response: **Răspuns și explicație (4 puncte):**

Integrează critic informațiile din Integrează critic(4p.) sursele propuse în propriul text. 0 p. - răspuns lipsă sau fără a face trimitere la surse; textul surselor este preluat fără a fi integrat în text; 1 p. – se fac unele încercări de a cita, de a face trim...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 90 (istorie) -- match ratio 0.62
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 3: F..."

Span A: `fără a face trimitere la`

Span B: `fără a fi integrat în`

Full response: **Răspuns și explicație (4 puncte):**

Integrează critic informațiile din Integrează critic(4p.) sursele propuse în propriul text. 0 p. - răspuns lipsă sau fără a face trimitere la surse; textul surselor este preluat fără a fi integrat în text; 1 p. – se fac unele încercări de a cita, de a face trim...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 1 (istorie) -- match ratio 0.61
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 2: D..."

Span A: `puncte abordate (cel puțin două).`

Span B: `cauză-efect/ interdependență (cel puțin două);`

Full response: **Răspuns și explicație (2 puncte):**

Formulează relații de cauză-efect (cel Menționează (2p.) puțin două). 0 p. – răspuns lipsă/ greșit; 1p. x2 - menționează cauze/ consecințe ale evenimentelor/ proceselor/fenomenelor 6 puncte abordate (cel puțin două). Formulează (4p.) 2p. x2 - formulează relații...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 6 (istorie) -- match ratio 0.61
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 2: A..."

Span A: `puncte abordate (cel puțin două).`

Span B: `cauză-efect/ interdependență (cel puțin două);`

Full response: **Răspuns și explicație (2 puncte):**

Formulează relații de cauză-efect (cel Menționează (2p.) puțin două). 0 p. – răspuns lipsă/ greșit; 1p. x2 - menționează cauze/ consecințe ale evenimentelor/ proceselor/fenomenelor 6 puncte abordate (cel puțin două). Formulează (4p.) 2p. x2 - formulează relații...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 11 (istorie) -- match ratio 0.61
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 2: D..."

Span A: `puncte abordate (cel puțin două).`

Span B: `cauză-efect/ interdependență (cel puțin două);`

Full response: **Răspuns și explicație (2 puncte):**

Formulează relații de cauză-efect (cel Menționează (2p.) puțin două). 0 p. – răspuns lipsă/ greșit; 1p. x2 - menționează cauze/ consecințe ale evenimentelor/ proceselor/fenomenelor 6 puncte abordate (cel puțin două). Formulează (4p.) 2p. x2 - formulează relații...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 79 (istorie) -- match ratio 0.61
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 2: D..."

Span A: `puncte abordate (cel puțin două).`

Span B: `cauză-efect/ interdependență (cel puțin două);`

Full response: **Răspuns și explicație (2 puncte):**

Formulează relații de cauză-efect (cel Menționează (2p.) puțin două). 0 p. – răspuns lipsă/ greșit; 1p. x2 - menționează cauze/ consecințe ale evenimentelor/ proceselor/fenomenelor 6 puncte abordate (cel puțin două). Formulează (4p.) 2p. x2 - formulează relații...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 84 (istorie) -- match ratio 0.61
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 2: S..."

Span A: `puncte abordate (cel puțin două).`

Span B: `cauză-efect/ interdependență (cel puțin două);`

Full response: **Răspuns și explicație (2 puncte):**

Formulează relații de cauză-efect (cel Menționează (2p.) puțin două). 0 p. – răspuns lipsă/ greșit; 1p. x2 - menționează cauze/ consecințe ale evenimentelor/ proceselor/fenomenelor 6 puncte abordate (cel puțin două). Formulează (4p.) 2p. x2 - formulează relații...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 89 (istorie) -- match ratio 0.61
Instruction: "Subiect: Istoria românilor și universală (Profil Umanist)

Itemul 2: D..."

Span A: `puncte abordate (cel puțin două).`

Span B: `cauză-efect/ interdependență (cel puțin două);`

Full response: **Răspuns și explicație (2 puncte):**

Formulează relații de cauză-efect (cel Menționează (2p.) puțin două). 0 p. – răspuns lipsă/ greșit; 1p. x2 - menționează cauze/ consecințe ale evenimentelor/ proceselor/fenomenelor 6 puncte abordate (cel puțin două). Formulează (4p.) 2p. x2 - formulează relații...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 145 (matematica) -- match ratio 0.60
Instruction: "Subiect: Matematică (Profil Real)

Itemul 1: Calculați valoarea expres..."

Span A: `8/125 • (−5)³ = −125`

Span B: `• (8/125)·(−125) = −8 •`

Full response: **Răspuns și explicație (5 puncte):**

Etape:
• (4/25)^1.5 = (2/5)³ = 8/125
• (−5)³ = −125
• (8/125)·(−125) = −8
• Răspuns: −8
• Punctaj: 5 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 77 (matematica) -- match ratio 0.57
Instruction: "Subiect: Matematică (Profil Real)

Itemul 12: Suma coeficienților bino..."

Span A: `• 120 − 6k −`

Span B: `= 0 ⟹ k =`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• C(n,1) + C(n,n−1) = 2n = 40 ⟹ n = 20
• Termenul general: T(k+1) = C(20,k)·x^(120−6k−2k/3)
• 120 − 6k − 2k/3 = 0 ⟹ k = 18
• T₁₉ = C(20,18) = 190
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 138 (limba_romana) -- match ratio 0.57
Instruction: "Subiect: Limba și literatura română

Context:
PROFIL UMANISTIC – 100 d..."

Span A: `accepta un text cu caracter`

Span B: `meditativ. 1 punct pentru caracterul`

Full response: **Răspuns și explicație (4 puncte):**

Meditează, în text coerent de 5-6 Se va accepta un text cu caracter 1+2+1 4 puncte rânduri, asupra afirmației: meditativ. 1 punct pentru caracterul meditativ al textului produs; „– Turnul ăsta e o axis mundi, aici. Așa ceva există în orice oraș 2 puncte pentru ...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 148 (matematica) -- match ratio 0.57
Instruction: "Subiect: Matematică (Profil Real)

Itemul 4: Rezolvați în ℝ inecuația:..."

Span A: `< x < 4/3 •`

Span B: `1/3] ∪ [1; 4/3) •`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• log₀.₂(x) = −log₅(x)
• log₅[x(4−3x)] ≤ 0 ⟹ x(4−3x) ≤ 1
• Condiții domeniu: 0 < x < 4/3
• Rezolvare: −3x²+4x−1 ≤ 0
• S = (0; 1/3] ∪ [1; 4/3)
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

### Record 73 (matematica) -- match ratio 0.56
Instruction: "Subiect: Matematică (Profil Real)

Itemul 8: Baza piramidei VABCD este..."

Span A: `• Se determină baza mare`

Span B: `• Se găsește centrul bazei`

Full response: **Răspuns și explicație (8 puncte):**

Etape:
• Se determină baza mare din datele trapezului
• Se găsește centrul bazei
• h = √(13² − d²) unde d = distanța centru-vârf
• Punctaj: 8 puncte...

**Verdict (fill in): [ ] Real duplication -- needs fixing  [ ] False positive (legitimate structure) -- no action

---

