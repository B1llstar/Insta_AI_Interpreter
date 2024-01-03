  @echo off
  REM Create the OInterpreter environment
  conda create -n OInterpreter -y --clone base
  conda activate OInterpreter

  REM Check and install dependencies
  for /F "tokens=1" %%a in ('conda list -- terse') do (
      set current_package=%%a
      set current_package_line=false
      for %%b in (%dependencies%) do (
          if /I "%%b"=="%%a" (
              set current_package_line=true
          )
      )
      if "%current_package_line%"=="true" (
          continue
      ) else (
          echo conda install -c anaconda %%a
      )
  )

  conda install -c anaconda python=3.9
  conda install -c anaconda openai-python
  conda install -c anaconda tqdm
  conda install -c anaconda nodejs
  conda install -c anaconda python-dotenv
  conda install -c anaconda pytz
  conda install -y -c anaconda pip
  conda install -y -c anaconda pip==21.2.4
  conda install -y -c anaconda pip-tools
  conda install -y -c anaconda pytest
  conda install -y -c anaconda pytest-cov
  conda install -c anaconda pytest-watch
  conda install -c anaconda pytest-timeout
  conda install -c anaconda pytest-randomly
  conda install -c anaconda pytest-pep8
  conda install -c anaconda pytest-littler
  conda install -c anaconda pytest-mock
  conda install -c anaconda pytestqt
  conda install -c anaconda pytest-dt

  REM Save the updated Anaconda terminal script
  echo "%windir%\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy ByPass -NoExit -Command "&
  'C:\Users\B1llstar\miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\B1llstar\miniconda3'; > conda_terminal_script.ps1

  REM Create a shortcut to the Anaconda terminal
  mklink /D "%USERPROFILE%\Desktop\Anaconda3 Terminal." "%USERPROFILE%\Desktop\Anaconda3 Terminal."