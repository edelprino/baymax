let g:ale_linters = {
\   'python': ['flake8'],
\}
let g:ale_python_flake8_executable = 'docker-compose exec baymax /root/.local/bin/flake8'

nmap <silent> <leader>r :terminal time docker-compose exec baymax python %<CR>
