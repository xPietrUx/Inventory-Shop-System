# CONTRIBUTING

## Workflow

### ✅ 1. Branchowanie — zasada: nie tykamy `main` bez powodu

-   **`main`** → zawsze działa, produkcja, demo, prezentacja → czysto.
-   Każdy nowy ficzer/poprawka → osobny branch.
-   Nazwa wg schematu: `feature/nazwa` albo `fix/opis`

Przykłady:

```
feature/dodanie-logowania
fix/poprawa-navbaru
```

### ✅ 2. Pull Requesty (PR)

-   Każdy PR → do `main`.
-   Opis PR zwięzły, co robisz:

```
Dodaje formularz rejestracji.
Fix #12 — naprawia przekierowanie po logowaniu.
```

-   Review → co najmniej 1 osoba klika „Approve” zanim zmergujesz.

### ✅ 3. Merge PR → zawsze `Squash and merge`

➡️ Dzięki temu cały PR = 1 commit na `main` → nie masz potem w historii miliona drobnych commitów typu „poprawka literówki”.

### ✅ 4. Co jak coś się zjebało?

➡️ NIE ROBIMY od razu `revert` na pałę.

Procedura:

1. Zakładasz branch: `fix/nazwa-fixu`
2. Robisz Pull Request → opisujesz, co poprawiasz.
3. Merge → czysto → życie idzie dalej.

### ✅ 5. Jak synchronizować branche przed PR (żeby nie było konfliktów)

➡️ Zanim otworzysz PR → zawsze robisz:

```
git checkout twoj-branch
git fetch origin
git rebase origin/main
```

Rozwiązujesz konflikty → dopiero wtedy pushujesz.

### ✅ 6. Konflikt → nie panikuj → rozwiąż lokalnie → `push --force-with-lease`

```
git push --force-with-lease
```

Nie `--force`, bo to topór. `--force-with-lease` → bezpieczniej.

### ✅ 7. Każdy robi pull PRZED pracą

```
git pull origin main
```

Zawsze. ZAWSZE.
