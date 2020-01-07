;; Set the command (Apple) key as Meta
(setq mac-command-modifier 'meta)

;; Initial language environment
(setq current-language-environment "UTF-8")

;; Initial frame size
(setq default-frame-alist '((top . 10) (left . 10) (width . 140) (height . 80)))

;; Always end a file with a newline
(setq require-final-newline t)

;; Stop at the end of the file, not just add lines
(setq next-line-add-newlines nil)

;; Show line number and column number
(setq line-number-mode t)
(setq column-number-mode t)

;; Fill column width
(setq default-fill-column 80)

;; Transient mark
(setq transient-mark-mode t)

;; Highlight trailing spaces
(setq-default show-trailing-whitespace t)

;; Turn toolbar off
(tool-bar-mode -1)

;; Turn auto-save off
(setq auto-save-list-file-prefix nil)

;; Use space instead of tab
(setq-default indent-tabs-mode nil)

;; Scale level +2 for plaintext writing
(add-hook 'text-mode-hook (lambda () (text-scale-adjust 2)))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 140 :width normal :foundry "unknown" :family "Andale Mono")))))
